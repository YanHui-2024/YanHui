import torch

@torch.jit.script
def f(x):  # ? x 6
    return x.t()[[0, 1, 5]]  # 3 x ?

print(f(torch.zeros((2, 6))))