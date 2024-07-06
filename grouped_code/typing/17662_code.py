import torch

def f():
    return torch.arange(5)

print(f().dtype)
print(torch.jit.script(f)().dtype)