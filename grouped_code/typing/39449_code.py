def foo(x: torch.Tensor, y):  # Missing "y: int"
    for _ in range(y):
        x = x + 1
    return x
        
x = torch.ones(())

foo_script = torch.jit.script(foo)
print(foo_script(x, 2))