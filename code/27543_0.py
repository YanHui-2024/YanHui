@torch.jit.script
def fn():
    a = [1, 2, 3, 4]
    return a[::-1]
fn()