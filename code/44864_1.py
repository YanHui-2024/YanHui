class A(nn.Module):
    def __init__(self):
        super().__init__()
        self.k = 1.0
    def forward(self, x):
        if self.training:
            assert not torch.jit.is_scripting(), "this codepath is not supported"
            return x * self.k if self.k != "test" else x   # error in torchscript due to type mistmatch
        else:
            return x + 1

a = A()
a = torch.jit.script(a)