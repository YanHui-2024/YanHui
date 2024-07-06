import torch

tensor = torch.IntTensor(4, 2).zero_()
print(len(tensor))  # prints 4

@torch.jit.script
def foo(tensor):
    print(len(tensor)) # this is dispatching to aten::len(Tensor[])
foo(tensor)  # prints 1