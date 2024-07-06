def t():
    x = [1,2,3]
    x = x[::-1]
    print(x)

torch.jit.script(t)()