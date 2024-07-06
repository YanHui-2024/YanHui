import torch

def foo(x):
  for i in range(10):
    x = torch.nn.functional.softmax(x)  # generates a warning inside

foo(torch.rand(5))

# warning is printed once

torch.jit.script(foo)(torch.rand(5))

# warning is printed 10 times