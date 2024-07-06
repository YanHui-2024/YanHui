import torch
@torch.jit.script
def func2(x, y):
    return x + y.type_as(x)
x = torch.tensor([0.1])
y = torch.tensor([1])
func2(x, y)

Out[8]: tensor([1.1000])