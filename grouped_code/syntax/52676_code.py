import torch
from torch.fx import symbolic_trace
from collections import namedtuple
from typing import Dict, NamedTuple, Optional, Tuple

class Point(NamedTuple):
    x: Optional[torch.Tensor] = None
    y: Optional[torch.Tensor] = None

class M(torch.nn.Module):
    def __init__(self):
        super(M, self).__init__()

    def forward(self, point: Point):
        return point

p = Point(x=torch.rand(3), y=torch.rand(3))
scripted = torch.jit.script(M())