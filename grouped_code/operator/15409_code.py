import torch
import torch.nn as nn

@torch.jit.script
def f(x):
    return nn.Softmax(dim=-1)(x)