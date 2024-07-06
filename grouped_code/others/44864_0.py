class A(nn.Module):
    def __init__(self):
        super().__init__()
        self.k = 1.0
    def forward(self, x):
        if self.training and not torch.jit.is_scripting():
            return x * self.k if self.k != "test" else x   # not supported due to lack of union type
        else:
            return x + 1

a = A()
a = torch.jit.script(a)