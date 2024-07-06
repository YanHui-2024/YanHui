import torch
from torch import nn

class Pad(torch.nn.Module):
    def forward(self, x):
        pad_op =  nn.ZeroPad2d(padding=(10, 20, 0, 0))
        return pad_op(x)

m = torch.jit.script(Pad())