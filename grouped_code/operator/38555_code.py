import torch


def reshape_test(t: torch.Tensor):
    t.reshape(-1)[0] = torch.tensor(1, dtype=t.dtype, device=t.device)

    return t


t = torch.zeros([2, 2])
print('PyTorch function result')
print(reshape_test(t))
print()

reshape_test = torch.jit.script(reshape_test)
t = torch.zeros([2, 2])
print('TorchScript function result')
print(reshape_test(t))
print()

print('TorchScript function graph')
print(reshape_test.graph)
