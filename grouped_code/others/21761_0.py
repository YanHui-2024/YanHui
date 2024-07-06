import torch

@torch.jit.script
class Foo(object):
    pass

@torch.jit.script
def foo():
    f = Foo()

print(foo.graph)