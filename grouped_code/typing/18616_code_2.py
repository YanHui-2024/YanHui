In [14]: @torch.jit.script
    ...: def g(x):
    ...:     return x[[1, 2]]
    ...:

In [15]: a = torch.arange(16).reshape(4,4)

In [16]: a
Out[16]:
tensor([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11],
        [12, 13, 14, 15]])

In [17]: g(x)
Out[17]: tensor(1.)

In [18]: print(g.code)
def forward(self,
    x: Tensor) -> Tensor:
  _0 = torch.select(torch.select(x, 0, 1), 0, 2)
  return _0