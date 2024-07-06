from torch import nn, jit, Tensor


class Bar(nn.ModuleDict):
    def forward(self, input: Tensor) -> Tensor:  # type: ignore[override]
        pass


bar = Bar()
jit.script(bar)