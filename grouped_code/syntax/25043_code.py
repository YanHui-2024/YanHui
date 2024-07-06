import torch

class Foo(torch.nn.Module):
    def forward(self, x):
        x = torch.neg(x)
# foo foo foo i have a comment at the wrong indent
        return x

torch.jit.script(Foo())