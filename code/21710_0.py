import torch
@torch.jit.script
def foo(x):
    return torch.sum(x, dim=1)