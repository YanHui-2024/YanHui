import torch
def f(x):
  return x*2
z = torch.jit.trace(f, (torch.zeros(10),))
print(type(z))