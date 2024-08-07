# this works
def fn(x):
    a = zeros_like(x, dtype=torch.uint8)
    a[torch.tensor(0)] = torch.tensor(2)
    return a

# this works
def fn(x):
    a = zeros_like(x, dtype=torch.uint8)
    a[0] = 2
    return a

# this  doesn't work
def fn(x):
    a = zeros_like(x, dtype=torch.uint8)
    a[torch.tensor(0)] = 2
    return a

x = torch.jit.script(fn)