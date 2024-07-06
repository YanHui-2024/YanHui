import torch

def foo():
    a = [1, 2, 3]
    b = list(a)
    a.pop()
    return a, b

foo_scripted = torch.jit.script(foo)

print(foo_scripted.code)
print('actual', foo_scripted())
print('expected', foo())
print(foo_scripted.graph_for())