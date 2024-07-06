import torch
string = "Normanðy"
print(string)

def foo(s: str):
    return len(s)

foo_scripted = torch.jit.script(foo)

print(foo(string))
print(foo_scripted(string))