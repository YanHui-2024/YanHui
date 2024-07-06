import torch
from torch import nn as nn

class M(torch.nn.Module):
    def __init__(self):
        super(M, self).__init__()
        self.weights = torch.nn.ParameterList([nn.Parameter(torch.randn(1)) for i in range(10)])

    def forward(self, x):
        return x

m = M()
torch.jit.trace(m, torch.randn(1))