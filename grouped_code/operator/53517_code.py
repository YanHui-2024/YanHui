import torch
from torch import fx

def foo(x):
    return x[..., :]

torch.jit.script(foo)  # ok
torch.jit.script(fx.symbolic_trace(foo))  # not ok