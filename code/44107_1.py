tensor([0.5000, 1.5000])
0.5
1.5
tensor([0., 1.])

def test(some_tensor: Tensor) -> Tensor:
  for loop_idx in range((torch.size(some_tensor))[0]):
    _0 = torch.select(some_tensor, 0, loop_idx)
    temp = torch.item(_0)
    print(temp)
    _1 = torch.select(some_tensor, 0, loop_idx)
    _2 = torch.copy_(_1, int(temp))
  return some_tensor