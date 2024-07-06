import torch

@torch.jit.script
def jit_warner(inp):
    return torch.nn.functional.sigmoid(inp) # triggers a deprecation warning

@torch.jit.script
def jit_ok(inp):
    return torch.sigmoid(inp)

class JitWarner(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x):
        return jit_warner(x)
        # return jit_ok(x) # this works

torch.onnx.export(JitWarner(), torch.randn(42), '/dev/null')