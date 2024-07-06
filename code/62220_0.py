@torch.jit.script
def foo(x):
     return [x, 1, 2, 3][0:2]