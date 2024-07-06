@torch.jit.script
def fn():
    x: int = 1
    x = "foo"
    return x