@torch.jit.script
def fn(m):
    # type: (Tensor) -> Device
    return m.device