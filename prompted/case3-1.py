import torch
import torch.nn as nn

class UnusualIndexingModel(nn.Module):
    def __init__(self):
        super(UnusualIndexingModel, self).__init__()
        self.linear = nn.Linear(10, 10)

    def forward(self, x):
        idx = torch.arange(x.size(0) - 1, -1, -1, dtype=torch.long)
        x = x.index_select(0, idx)
        x = self.linear(x)
        return x

model = UnusualIndexingModel()
scripted_model = torch.jit.script(model)

input_tensor = torch.randn(5, 10)
output1 = model(input_tensor)
output2 = scripted_model(input_tensor)
print("Original PyTorch model output:", output1)
print("Scripted TorchScript model output:", output2)

