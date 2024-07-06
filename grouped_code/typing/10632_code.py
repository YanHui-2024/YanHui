import torch

@torch.jit.script
def create_zeros():
    return torch.zeros(1, 2, 3, dtype=torch.long)