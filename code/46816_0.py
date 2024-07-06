import torch
import torch.nn as nn

class MyModule(nn.Module):
    def __init__(self, use_memory_efficent):
        super(MyModule, self).__init__()
        self.use_memory_efficent = use_memory_efficent

    @torch.jit.unused
    def memory_efficient(self, x):
        import pdb
        pdb.set_trace()
        return x + 10

    def forward(self, x):
        # Use not-yet-scriptable memory efficient mode
        if self.use_memory_efficient:
            return self.memory_efficient(x)
        else:
            return x + 10

m = torch.jit.script(MyModule(use_memory_efficent=False))
m.save("m.pt")

m = torch.jit.script(MyModule(use_memory_efficient=True))
# exception raised
m(torch.rand(100))