import torch
class ConstantTensor(torch.jit.ScriptModule):
    def __init__(self):
        self.cx = torch.ones(100, 100, dtype=torch.float, device='cuda')

    @torch.jit.script_method
    def forward(self, x):
        return x + self.cx


c = ConstantTensor()
print c.graph
