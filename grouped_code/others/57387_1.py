@torch.jit.script
def foo(x: bool):
    return x  is True, x == True

torch._C._jit_pass_cse(foo.graph)
torch._C._jit_pass_dce(foo.graph)
print(foo.graph)