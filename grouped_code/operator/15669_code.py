import torch

@torch.jit.script
def foo(x):
    chunked = torch.chunk(x, 2)
    foo = chunked[0]
    foo.add_(5)

foo(torch.zeros(12))