def func(x):
    s = 0
    s += x
    s += x
    return s
x = torch.ones(2,2)
func = torch.jit.trace(func, x)
print('x',x) # tensor([[1., 1.], [1., 1.]]) as expected
_ = func(x)
print('x',x) # tensor([[2., 2.], [2., 2.]])  surprisingly x have changed while it shouldn't!