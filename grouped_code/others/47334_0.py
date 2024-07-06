class A(nn.Module):
    def __init__(self):
        super().__init__()
        self.x = tuple([0, 1, 2])
        self.y = nn.ModuleList([nn.Linear(10, 10)] * 3)

    def forward(self, x):
        return self.x[::-1][0] + x

a = A()
script = torch.jit.script(a)