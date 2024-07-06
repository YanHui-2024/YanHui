import torch
from collections import namedtuple
_MyNamedTuple = namedtuple('_MyNamedTuple', ['value'])

@torch.jit.script
def foo():
    return _MyNamedTuple(1)
> Expected a value of type 'Tensor' for argument 'value' but instead found type 'int'.