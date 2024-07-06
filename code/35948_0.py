def f(s: str):
    return int(s)
f = torch.jit.script(f)