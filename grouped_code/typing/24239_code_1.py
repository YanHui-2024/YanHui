def channel(tensor: torch.Tensor) -> torch.Tensor:
    a = torch.randn(2)
    return a[tensor.long()]

@torch.jit.script
def full():
    l = []
    for _ in range(3):
        l.append(channel(torch.randn(1, 3, 3) > 0))
    torch.stack(l)