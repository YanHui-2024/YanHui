import torch
from typing import NamedTuple

class Params(NamedTuple):
    p1: float
    p2: int

params = Params(1.0, 2)

@torch.jit.script
def f(params: Params):
    print(params.p1)

f(params)