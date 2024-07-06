import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Linear(768, 100000)

    def forward(self, x):
        x = x * 2
        x = x * 2
        x = x * 2
        x = self.fc(x)
        return x

# trace on cpu
m = Net()
x = torch.randn(10, 128, 768)
jm = torch.jit.trace(m, x)
jm = jm.to("cuda")

for i in range(0,2):
    x = torch.randn(10, 128, 768, requires_grad=True).to("cuda")
    y = jm(x)
    tgt = torch.randn_like(y)
    y.backward(tgt)