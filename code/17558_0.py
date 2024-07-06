@torch.jit.script
def b(x: Optional[Tuple[int, int]] = None):
    if x is None:
        x = (1, 2)
    else:
        x = torch.jit._unwrap_optional(x)
        
    return x