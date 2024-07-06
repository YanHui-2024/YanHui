RuntimeError:
arguments for call are not valid:

  for operator aten::copy_(Tensor t, Tensor other) -> Tensor:
  argument other not provided.
  @torch.jit.script
  def foo(x):
      y = torch.rand(3, 4)
      y.copy_(x)
      ~~~~~~ <--- HERE
      return y

  for operator aten::copy_(Tensor t, int other) -> Tensor:
  argument other not provided.
  @torch.jit.script
  def foo(x):
      y = torch.rand(3, 4)
      y.copy_(x)
      ~~~~~~ <--- HERE
      return y

  for operator aten::copy_(Tensor t, float other) -> Tensor:
  argument other not provided.
  @torch.jit.script
  def foo(x):
      y = torch.rand(3, 4)
      y.copy_(x)
      ~~~~~~ <--- HERE
      return y
for call at:
@torch.jit.script
def foo(x):
    y = torch.rand(3, 4)
    y.copy_(x)
    ~~~~~~ <--- HERE
    return y