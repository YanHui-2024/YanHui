import torch

@torch.jit.script
def method1(x, weight, b1, b2):
    bias = b1 * b2
    return torch.nn.functional.linear(x, weight, bias)

M = 10
K = 10
N = 10

x = torch.rand(M, K, requires_grad=True)
weight = torch.rand(K, N, requires_grad=True)
b1 = torch.rand(M, N, requires_grad=True)
b2 = torch.rand(M, N, requires_grad=True)

method1(x, weight, b1, b2)
method1(x, weight, b1, b2)