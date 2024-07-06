@torch.jit.script
def b(x: Optional[int] = None):
    if x is None:
        x = 1
    else:
        x = torch.jit._unwrap_optional(x)
        
    return x