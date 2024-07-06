import torch

@torch.jit.script
def norm_test():
  t = torch.ones(10, 5)
  return torch.norm(t, dim=1, keepdim=True)