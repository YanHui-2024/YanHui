@torch.jit.script
def f():
    x = [i for i in range(5)]
    print(x)