import torch

@torch.jit.script
def foo(x):
    y = torch.rand(3, 4)
    y.copy_(x)
    return y
