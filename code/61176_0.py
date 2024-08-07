import torch
from torch import nn

class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        self.module_list = nn.ModuleList([nn.Linear(1,1) for _ in range(10)])
        self.parameter_list = nn.ParameterList([nn.Parameter(torch.zeros(1)) for _ in range(10)])

    def forward(self, x):
        self.module_list[0]
        self.parameter_list[0]
        return x


if __name__ == '__main__':
    model = MyModule()
    torch.jit.script(model)