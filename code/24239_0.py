def channel(tensor: torch.Tensor) -> torch.Tensor:
    a = torch.randn(2)
    return a[tensor.long()]

@torch.jit.script
def full():
    torch.stack([channel(torch.randn(1, 3, 3) > 0) for _ in [0, 1, 2]])