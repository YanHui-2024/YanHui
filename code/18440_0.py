import torch

@torch.jit.script
def foo(x):
    for i in range(1, 10):
        x += float(i)
    return x

print(foo.code)