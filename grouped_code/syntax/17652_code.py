import torch

@torch.jit.script
def f(a):
    return a[0].item() == 1