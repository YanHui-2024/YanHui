import torch
from torch import nn

class Model(nn.Module):
    def __init__(self, h: int = 16) -> None:
        super().__init__()
        self.fc1 = nn.Linear(h, h)

    @torch.jit.script
    def forward(self, x: torch.Tensor):
        return torch.tanh(self.fc1(x))
    
m = Model(42)
y = m(torch.randn(42, 42))
