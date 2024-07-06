import torch

def foo():    
    return round(2.5)

sfoo = torch.jit.script(foo)
print(foo(), sfoo())
# gives
# 2, 3.0