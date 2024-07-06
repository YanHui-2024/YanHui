import torch

def f(x, y, z):
    return ((x + y) / z) >= z

inputs = [torch.randn(2, 2, device='cuda') for _ in range(3)]
real_output = f(*inputs)
fs = torch.jit.script(f)
output = fs(*inputs)
print(fs.graph_for(*inputs))
print(output)
print(real_output)