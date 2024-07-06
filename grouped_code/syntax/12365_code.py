@torch.jit.script
def f(x):
    return torch.sort(x)[0]