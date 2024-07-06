import torch

@torch.jit.script
def cast_to_int(x):
    return x.int()