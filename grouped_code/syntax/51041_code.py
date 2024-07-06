import torch
from typing import Optional, List


class ToScript(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.foo = torch.jit.annotate(Optional[List[int]], None)
        # also doesn't work
        # self.foo : Optional[List[int]] = None

    def forward(self, x: List[int]):
        self.foo = x
        return 1


torch.jit.script(ToScript())