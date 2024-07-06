import torch

@torch.jit.script
def capture_bug(x):
    output = 0
    for i in range(20):
        if i == 0:
            output = x.unsqueeze(0)
        else:
            output = torch.cat((output, x.unsqueeze(0)), dim=0)
    return output

print(capture_bug.graph)