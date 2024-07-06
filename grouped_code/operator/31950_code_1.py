@torch.jit.script
def fn(m: Tensor) -> torch.Device:
    return m.device