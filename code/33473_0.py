import torch as tc
from torch import jit
@jit.script
def func(inp):
    return inp<<1
a = tc.tensor([3,4,5])
func(a)