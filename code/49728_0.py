class MyModule(torch.nn.Module):
    flag: torch.jit.Final[bool]

    def __init__(self):
        super().__init__()
        self.flag = True

    def forward(self) -> torch.Tensor:
        if self.flag:
            return torch.ones(3)
        else:
            return {}