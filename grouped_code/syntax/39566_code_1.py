import torch
#from typing import Final
from torch.jit import Final

class M(torch.nn.Module):
    y: Final[float]

    def __init__(self):
        super().__init__()
        self.y = 0.0

    def forward(self, x):
        return x + self.y

torch.jit.script(M())