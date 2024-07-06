import torch
from typing import Optional

class MyModule(torch.nn.Module):
    submod: Optional[torch.nn.Linear]

    def __init__(self):
        super(MyModule, self).__init__()
        self.submod = None

    def init_params(self, input):
        # NOTE: This function is called *before* forward (by another caller function),
        # not *by* forward, so it's not scripted.
        # In fact, you can remove this `init_params` function and see the same segfault.
        self.submod = torch.nn.Linear(input[-1], 5)
    
    def forward(self, input):
        submod = self.submod
        assert submod is not None
        return submod(input)
    
m = MyModule()
print(torch.jit.script(m))