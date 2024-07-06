@torch.jit.script
def foo(s: Any):
    if isinstance(s, dict):
        print(s.items())