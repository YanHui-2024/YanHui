import torch

@torch.jit.script
def f(x):
    return torch.autograd.grad([x.sum()], [x], retain_graph=True)