import torch
import torch.nn as nn

class A(nn.Module):
    def __init__(self):
        super().__init__()
        self.x: int = 0    # int field
    def forward(self):
        self.x += 1       # fails to script
        return self.x