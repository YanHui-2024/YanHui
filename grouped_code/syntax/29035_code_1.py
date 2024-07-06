import torch
import torch.nn as nn

import a

class M(nn.Module):
    def forward(self) -> a.Type:
        return a.Type(1)

torch.jit.script(M())