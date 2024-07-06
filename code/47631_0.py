import torch
from typing import Any

@torch.jit.interface
class ModuleInterface(torch.nn.Module):
    def forward(self, inputs: torch.Tensor) -> Any:
        pass

class TestModule(torch.nn.Module):
    def __init__(self):
        super(TestModule, self).__init__()

    def forward(self, inputs: Any) -> Any:
        return inputs

class Mod(torch.nn.Module):
    def __init__(self):
        super(Mod, self).__init__()
        self.d = torch.nn.ModuleDict({"module": TestModule()})

    def forward(self, x: Any, key: str) -> Any:
        value: ModuleInterface = self.d[key]
        return value.forward(x)

# this fails with "Attribute module is not of annotated type ModuleInterface".
m = Mod()
torch.jit.script(m)