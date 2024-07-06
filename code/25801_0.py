@torch.jit.script
def fn(x):
    # type: (List[int], int) -> bool
    return max(x)