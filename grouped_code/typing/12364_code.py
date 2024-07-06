import torch

@torch.jit.script
def f(x):
    return torch.zeros(5, device=x.device)

x = torch.rand(2,3,4)
print(f(x))