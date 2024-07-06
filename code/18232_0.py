@torch.jit.script
def fn(x, y):
    # type: (Dict[int, int], int) -> int
    return x.get(y, 3)

@torch.jit.script
def fn(x, y):
    # type: (Dict[int, int], int) -> int
    if y in x:
        return x[y]
    else:
        return 3

d = {1: 2, 3: 4}
print(fn.graph)
print(fn(d, 3))
print(fn(d, 2))