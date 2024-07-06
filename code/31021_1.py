import torch

@torch.jit.script
def foo(x: torch.Tensor) -> torch.Tensor:
    return torch.isinf(x)