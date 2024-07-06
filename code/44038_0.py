import torch
from typing import Tuple

class TestModule(torch.nn.Module):
    def __init__(self):
        super(TestModule, self).__init__()

    def forward(self, ids: Tuple[int]) -> int:
        return hash(ids)

scripted_module = torch.jit.script(TestModule())
ret = scripted_module((1, 2))