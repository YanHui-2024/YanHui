import torch

def f(x: complex, y: torch.Tensor):
    o = torch.add(x, y)
    o = 2 + o
    return o

jf = torch.jit.script(f)
x = 1j
y = torch.tensor(5j, device='cuda')

print(f(x, y))
print(jf(x, y))
print(jf.graph)
print(jf.graph_for(x, y))