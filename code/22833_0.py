import torch

def f(z):
    return (torch.ones(2) * z ** 2 - z).sum()

torch.set_default_tensor_type(torch.cuda.FloatTensor)
jf = torch.jit.trace(f, torch.tensor(1.))

z = torch.tensor(1., requires_grad=True)
y = jf(z)
print(torch.autograd.grad(y, (z,))[0])

z = torch.tensor(1., requires_grad=True)
y = f(z)
print(torch.autograd.grad(y, (z,))[0])