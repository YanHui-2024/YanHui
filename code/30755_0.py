class M(nn.Module):
    @staticmethod
    def some_method(x):
        return x + 10

    def forward(self, x):
        return self.some_method(x)

torch.jit.script(M())