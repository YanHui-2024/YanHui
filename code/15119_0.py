import torch
import torch.nn as nn


class M(torch.jit.ScriptModule):

    def __init__(self):
        super(M, self).__init__()
        self.softmax = nn.Softmax(dim=0)

    @torch.jit.script_method
    def forward(self, v):
        return self.softmax(v)

i = torch.Tensor(2)
m = M()
o = m(i)