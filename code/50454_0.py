import torch
from torch import nn
class A(nn.Module):
    def forward(self, x):
        return x * 2
print(torch.__version__)
model = A()
trace = torch.jit.trace(model, torch.tensor([3]))
print(trace.inlined_graph)
n = trace.inlined_graph.nodes()
print(list(n))