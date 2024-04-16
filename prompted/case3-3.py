import torch
import torch.nn as nn

class ComplexDataStructuresModel(nn.Module):
    def __init__(self):
        super(ComplexDataStructuresModel, self).__init__()
        self.linear1 = nn.Linear(10, 20)
        self.linear2 = nn.Linear(20, 30)

    def forward(self, x):
        layer_dict = {"linear1": self.linear1, "linear2": self.linear2}
        x = layer_dict["linear1"](x)
        x = torch.relu(x)
        x = layer_dict["linear2"](x)
        return x

model = ComplexDataStructuresModel()
scripted_model = torch.jit.script(model)

input_tensor = torch.randn(1, 10)
output1 = model(input_tensor)
output2 = scripted_model(input_tensor)
print("Original PyTorch model output:", output1)
print("Scripted TorchScript model output:", output2)

