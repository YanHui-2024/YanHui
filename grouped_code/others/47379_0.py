class A(nn.Module):
    def forward(self, x):
        if torch.jit.is_scripting() or not torch.jit.is_tracing():
            return x + 1
        else:
            return x + 2

a = A()
script = torch.jit.script(a)