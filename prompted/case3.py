import torch
import torch.nn as nn

class NestedControlFlowModel(nn.Module):
    def __init__(self):
        super(NestedControlFlowModel, self).__init__()
        self.linear = nn.Linear(10, 10)

    def forward(self, x):
        if x.sum() > 0:
            for _ in range(int(x[0, 0].item())):
                x = self.linear(x)
        else:
            x = -x
        return x

model = NestedControlFlowModel()
scripted_model = torch.jit.script(model)

input_tensor = torch.randn(1, 10)
output1 = model(input_tensor)
output2 = scripted_model(input_tensor)
print("Original PyTorch model output:", output1)
print("Scripted TorchScript model output:", output2)

