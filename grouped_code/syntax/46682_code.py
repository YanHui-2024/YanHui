import torch
from torch import nn

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self):
        return "a" in "abcd"

m = MyModel()
scripted = torch.jit.script(m)
scripted()