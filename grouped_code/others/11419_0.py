$ cat mwe.py 
import torch
@torch.jit.script
def f(x):
    return torch.tanh(x)
$ python mwe.py
