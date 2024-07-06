import torch
@torch.jit.script
def fn(x, y, z):
    x1 = x + y 
    y1 = x - y
    w = torch.cat([x1, y1])
    return w + z

x = torch.randn(2, 2, dtype=torch.float, device='cpu')
y = torch.randn(2, 2, dtype=torch.float, device='cpu')
z = torch.randn(4, 2, dtype=torch.float, device='cpu')
fn(x, y, z)
fn.graph_for(x, y, z)