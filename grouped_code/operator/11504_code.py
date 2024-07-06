def fn(mean, std):
    return torch.normal(mean, std)

compiled_fn = torch.jit.trace(fn, (torch.zeros(2, 3), torch.ones(2, 3)))