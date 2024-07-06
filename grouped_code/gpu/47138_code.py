import torch
from torch import nn
from torch.nn import functional as F

dtype = torch.float16
device = torch.device("cuda", 0)


class MockSEFixupBasicBlock(nn.Module):
    def __init__(self, inplanes, planes):
        super().__init__()

        self.fixup_bias2a = nn.Parameter(torch.zeros(1))
        self.fixup_scale = nn.Parameter(torch.ones(1))
        self.fixup_bias2b = nn.Parameter(torch.zeros(1))

    def forward(self, x):
        identity = x
        out = x

        out = out + self.fixup_bias2a
        out = out * self.fixup_scale + self.fixup_bias2b

        return out * out + identity


net = torch.jit.script(MockSEFixupBasicBlock(64, 64)).to(dtype=dtype, device=device)

inp = torch.randn(16, 64, 16, 16, dtype=dtype, device=device)

for i in range(10):
    for param in net.parameters():
        param.grad = None

    print(i)
    net(inp).mean().backward()
