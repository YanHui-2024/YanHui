def forward(self,
    x: Tensor) -> Tensor:
  _0 = torch.select(torch.select(x, 0, 1), 0, 2)
  _1 = torch.copy_(_0, 1)
  return x