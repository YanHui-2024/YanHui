import torch

def foo(x: torch.Tensor, y: torch.Tensor, W: torch.Tensor):
    return torch.exp(torch.mm(torch.complex(x, y), W.cfloat()))

@torch.jit.script
def jitted_foo(x: torch.Tensor, y: torch.Tensor, W: torch.Tensor):
    return torch.exp(torch.mm(torch.complex(x, y), W.cfloat()))

x = torch.randn(128, 16, dtype=torch.float32, device='cuda:0')
y = torch.randn(128, 16, dtype=torch.float32, device='cuda:0')
W = torch.randn(16, 1, dtype=torch.float32, device='cuda:0', requires_grad=True)
W.data /= 4
print('1st launch - foo(...).grad_fn is None = {}'.format(foo(x, y, W).grad_fn is None)) # outputs False, which is what's expected
print('2nd launch - foo(...).grad_fn is None = {}'.format(foo(x, y, W).grad_fn is None)) # outputs False, again as expected
print('1st launch - jitted_foo(...).grad_fn is None = {}'.format(jitted_foo(x, y, W).grad_fn is None)) # outputs False, again as expected
print('2nd launch - jitted_foo(...).grad_fn is None = {}'.format(jitted_foo(x, y, W).grad_fn is None)) # outputs True, meaning the graph is lost