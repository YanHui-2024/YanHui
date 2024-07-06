import torch

@torch.jit.script
def fn():
    perm = torch.randperm(2)
    print("inferred dtype: %d" % perm.dtype)
    perm = torch.randperm(2, dtype=torch.int64)
    print("dtype with int64 is set: %d" % perm.dtype)

fn()