import torch
from typing import Dict

class AttributeModule(torch.nn.Module):
    def __init__(self):
        super(torch.nn.Module, self).__init__()
        self.foo = torch.jit.Attribute(0.1, float)

        # we should be able to use self.foo as a float here
        assert 0.0 < self.foo

        self.names_ages = torch.jit.Attribute({}, Dict[str, int])
        self.names_ages["someone"] = 20
        assert isinstance(self.names_ages["someone"], int)

m = AttributeModule()