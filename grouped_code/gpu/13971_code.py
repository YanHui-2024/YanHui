@torch.jit.script
def x(a):
     return a.abs()*2
x(torch.randn(5, device='cuda'))