@torch.jit.trace(torch.ones(2, 3), torch.ones(2, 3))
def fn(x, y):
    return torch.einsum('ab,ab->b', [x, y])


fn(torch.ones(2, 3), torch.ones(2, 3))