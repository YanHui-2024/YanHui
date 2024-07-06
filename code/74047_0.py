import torch

class Model(torch.nn.Module):
    def forward(self, x):
        return torch.ones(x.numel())

x = torch.randn(2, 3, 4)
g = torch.jit.trace(Model(), (x, ))
print(g.graph)