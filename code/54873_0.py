import torch
from typing import List

def fn():
    x: List[torch.Tensor] = []
    if torch.jit.isinstance(x, List[int]):
        print("Wrong!")
    else:
        print("Right")
    return x

scripted = torch.jit.script(fn)
scripted()                 # prints "Right"
fn()                       # prints "Wrong!"