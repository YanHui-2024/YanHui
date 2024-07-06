import copy
import torch
import torch.nn as nn
from torchvision import models


class ReNet(nn.Module):

    def __init__(self, n_input, n_units):
        super(ReNet, self).__init__()

        self.rnn = nn.GRU(n_input, n_units,
                          num_layers=1, batch_first=False,
                          bidirectional=True)

    def rnn_forward(self, x):

        b, n_height, n_width, n_filters = x.size()

        x = x.view(b * n_height, n_width, n_filters)
        x = x.permute(1, 0, 2)
        x, _ = self.rnn(x)
        x = x.permute(1, 0, 2)
        x = x.view(b, n_height, n_width, -1)

        return x

    def forward(self, x):
                                       #b, nf, h, w
        x = x.permute(0, 2, 3, 1)      #b, h, w, nf
        x = self.rnn_forward(x)        #b, h, w, nf
        x = x.permute(0, 3, 1, 2)      #b, nf, h, w

        return x


class Architecture(nn.Module):

    def __init__(self):
        super(Architecture, self).__init__()

        self.cnn = models.resnet50(pretrained=True)
        self.cnn = nn.Sequential(*list(self.cnn.children())[:-5])

        self.renet1 = ReNet(256, 50)

    def forward(self, x):
        x = self.cnn(x)
        x = self.renet1(x)

        return x


def compare_models(cpu_model, gpu_model):

    is_identical = True

    cpu_model_state_dict = cpu_model.state_dict()
    gpu_model_state_dict = gpu_model.state_dict()

    for param_key, cpu_params in cpu_model_state_dict.items():
        gpu_params = gpu_model_state_dict[param_key]
        _identical = torch.all(gpu_params == cpu_params.to(torch.device("cuda")))
        if _identical.item() == 0:
            print("\n\t# PARAMETER : ", param_key)
            print("\t* GPU : ", gpu_params.view(-1)[:5])
            print("\t* CPU : ", cpu_params.view(-1)[:5])
            is_identical = False

    return is_identical


def trace(model, usegpu):
    with torch.set_grad_enabled(False):
        model.eval()

        dummy_input = torch.randn(1, 3, 224, 224)
        
        if usegpu:
            dummy_input = dummy_input.to(torch.device('cuda'))

        traced_model = torch.jit.trace(model, dummy_input)

    return traced_model


torch.manual_seed(13)

model_cpu = Architecture()
model_gpu = copy.deepcopy(model_cpu).to(torch.device("cuda"))

print("STEP 1 : ", compare_models(model_cpu, model_gpu))

traced_model_cpu = trace(model_cpu, False)
traced_model_gpu = trace(model_gpu, True)
print("STEP 2 : ", compare_models(traced_model_cpu, traced_model_gpu))
print("STEP 2 : ", compare_models(traced_model_gpu, model_gpu))

torch.jit.save(traced_model_cpu, "model_cpu.pth")
torch.jit.save(traced_model_gpu, "model_gpu.pth")
print("STEP 3 : ", compare_models(traced_model_cpu, traced_model_gpu))
print("STEP 3 : ", compare_models(traced_model_gpu, model_gpu))

traced_model_cpu_loaded = torch.jit.load("model_cpu.pth")
traced_model_gpu_loaded = torch.jit.load("model_gpu.pth")
print("\nSTEP 4 : ", compare_models(traced_model_cpu_loaded, model_cpu))
print("\nSTEP 4 : ", compare_models(traced_model_gpu_loaded, model_cpu))