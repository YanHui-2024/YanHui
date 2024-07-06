class A(nn.Module):
    def __init__(self):
        super().__init__()
        self.k = 1.0
    def forward(self, x):
        if self.training:
            if not torch.jit.is_scripting():
                return x * self.k if self.k != "test" else x
            else:
                assert False, "this codepath is not supported"
        else:
            return x + 1