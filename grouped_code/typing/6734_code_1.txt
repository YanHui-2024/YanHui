@torch.jit.script
def func(x):
  return torch.nn.functional.adaptive_avg_pool1d(x, output_size=[1])