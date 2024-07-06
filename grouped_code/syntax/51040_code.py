import torch

@torch.jit.script
def test():
    c = 0
    for i in range(4):
        c += 10
    else:
        print("In else block of for...else")
    return c
      
print(test())
