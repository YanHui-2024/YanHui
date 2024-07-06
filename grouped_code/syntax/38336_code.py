@torch.jit.script
def mm(a,b):
    a %= b
    return a