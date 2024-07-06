graph(%self : __torch__.Model,
      %x : Float(2, 3, 4, strides=[12, 4, 1], requires_grad=0, device=cpu)):
  %4 : int = prim::Constant[value=24]() # repro_march_numel.py:5:0
  %5 : int[] = prim::ListConstruct(%4)
  %6 : int = prim::Constant[value=6]() # repro_march_numel.py:5:0
  %7 : NoneType = prim::Constant()
  %8 : Device = prim::Constant[value="cpu"]() # repro_march_numel.py:5:0
  %9 : bool = prim::Constant[value=0]() # repro_march_numel.py:5:0
  %10 : Float(24, strides=[1], requires_grad=0, device=cpu) = aten::ones(%5, %6, %7, %8, %9) # repro_march_numel.py:5:0
  return (%10)