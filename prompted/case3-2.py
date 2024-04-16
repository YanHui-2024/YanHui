import torch
import torch.nn as nn

class InPlaceModificationModel(nn.Module):
    def __init__(self):
        super(InPlaceModificationModel, self).__init__()
        self.linear = nn.Linear(10, 10)

    def forward(self, x):
        x = self.linear(x)
        x.clamp_(min=0)  # In-place ReLU
        return x

model = InPlaceModificationModel()
scripted_model = torch.jit.script(model)

input_tensor = torch.randn(1, 10)
output1 = model(input_tensor)
output2 = scripted_model(input_tensor)
print("Original PyTorch model output:", output1)
print("Scripted TorchScript model output:", output2)

