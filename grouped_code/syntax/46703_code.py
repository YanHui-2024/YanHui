import torch

class A(torch.nn.Module):
    good: torch.jit.Final[bool]
    def __init__(self):
        super().__init__()
        self.good = True
    def forward(self, x):
        #if hasattr(self, 'good'):  # works
        #if True:  # fails
        #if self.good is not None:  # works
        if self.good:  # fails
            return x

        # imagine below are some code that are scriptable depend on the availability of self.good
        print("hello") + 2  # shall not be compiled

x = A()
f = torch.jit.script(x)
f.forward(torch.randn(3))