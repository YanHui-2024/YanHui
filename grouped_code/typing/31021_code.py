Return value was annotated as having type Tensor but is actually of type bool:
at x.py:5:4
@torch.jit.script
def foo(x: torch.Tensor) -> torch.Tensor:
    return torch.isinf(x)