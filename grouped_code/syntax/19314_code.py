import torch

# works
def foo(x):
    rv = x[0]
    for x_i in x:
        rv += x_i
    return rv

print(foo(torch.rand(3, 4, 5)))

# doesn't work
@torch.jit.script
def foo(x):
    rv = x[0]
    for x_i in x:
        rv += x_i
    return rv

print(foo(torch.rand(3, 4, 5)))