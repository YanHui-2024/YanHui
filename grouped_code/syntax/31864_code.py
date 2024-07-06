import torch as T

from collections import namedtuple
from typing import Tuple
GG = namedtuple('GG', ['f', 'g'])

class Foo(nn.Module):
    def __init__(self):
        super().__init__()

    @T.jit.ignore
    def foo(self, x, z) -> GG:
		# Above does NOT work

        # ! type: (Tensor, Tensor) -> GG
        # Above works

		# ! type: (Tensor, Tensor) -> Tuple[GG, GG]
		# return GG(x, z), GG(x, z)
		# Above does NOT work

        return GG(x, z)
    def forward(self, x, z):
        y0, y1 = self.foo(x, z)
        return y0 + y1

foo = T.jit.script(Foo())
y = foo(T.randn(100, 100), T.randn(100, 100))