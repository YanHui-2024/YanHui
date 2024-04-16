import torch


def fn(x):
    # v1: [3, 1, 7, 7] alias of x
    v1 = torch.Tensor.transpose_(x, 0, 1)
    # v2: [3, 1, 7, 7] alias of x
    v2 = torch.Tensor.contiguous(x, memory_format=torch.channels_last)
    return v1, v2


# There are a few ways for making it "work":
# 1. Remove `memory_format=torch.channels_last` from `torch.Tensor.contiguous`
# 2. Add any non-inplace of before `transpose_` such as `x = torch.relu(x)`
# 3. Add any non-inplace operator after `torch.Tensor.contiguous` such as `torch.cos`
# 4: Use any shape-preserving inplace op to replace `transpose_` such as `torch..relu_`
# 5. Only return v1 or v2 not both.
# 6. Let the input channel dimension to be 1 instead of something greater than 1.
# 7. Use `check_trace=False` in `torch.jit.trace`

# eager
res = fn(torch.rand([1, 2, 4, 4]))
print("Eager mode... Success!")
# compile
torch.jit.trace(fn, torch.rand([1, 2, 4, 4]))
