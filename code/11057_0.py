import torch

@torch.jit.trace(torch.rand(3, 4))
def foo(x):
    pass