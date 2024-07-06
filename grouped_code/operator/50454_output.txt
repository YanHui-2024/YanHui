1.8.0a0+5cd04d2
graph(%self : __torch__.A,
      %x : Long(1, strides=[1], requires_grad=0, device=cpu)):
  %2 : Long(requires_grad=0, device=cpu) = prim::Constant[value={2}]() # a.py:8:0
  %3 : Long(1, strides=[1], requires_grad=0, device=cpu) = aten::mul(%x, %2) # a.py:8:0
  return (%3)

zsh: segmentation fault (core dumped)  python3 a.py