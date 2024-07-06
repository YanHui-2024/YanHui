import torch
import torch.nn as nn

class AtenSoftmaxRepalce(nn.Module):
    def __init__(self, dim=-1):
        super(AtenSoftmaxRepalce, self).__init__()
        self.conv = torch.nn.Conv2d(3, 64, (3, 3), stride=(2, 2), padding=(1, 1), bias=False)
        self.softmax = torch.nn.Softmax(dim)

    def forward(self, x):
        x1 = self.conv(x)
        return self.softmax(x1)

model = AtenSoftmaxRepalce()
model.eval()

x = torch.rand(1, 3, 224, 224).to(torch.bfloat16)

with torch.no_grad():
    with torch.cpu.amp.autocast(cache_enabled=False):
        model = torch.jit.trace(model, x).eval()