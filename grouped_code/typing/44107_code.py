import torch


@torch.jit.script
def test(some_tensor: torch.Tensor):
    for loop_idx in range(some_tensor.shape[0]):
        temp = some_tensor[loop_idx].item()
        print(temp)
        some_tensor[loop_idx] = temp

    return some_tensor


some_tensor = torch.Tensor([0.5, 1.5])
print(some_tensor)
print(test(some_tensor), '\n')
print(test.code)