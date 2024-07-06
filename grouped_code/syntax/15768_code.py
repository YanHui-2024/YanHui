@torch.jit.script
def test():
    return 1 // 0


print(test())