graph(%input.1 : Float(2, 8, strides=[8, 1], requires_grad=1, device=cpu),
      %bias.1 : Float(8, strides=[1], requires_grad=0, device=cpu)):
  %2 : Float(8, strides=[1], requires_grad=0, device=cpu), %3 : Float(2, 8, strides=[8, 1], requires_grad=1, device=cpu), %4 : bool = prim::RequiresGradCheck[types=[Tensor(re
quires_grad=0), Tensor(requires_grad=1)]](%bias.1, %input.1)
  %5 : Tensor = prim::If(%4)
    block0():
      %6 : Tensor = prim::DifferentiableGraph_0(%2, %3)
      -> (%6)
    block1():
      %7 : Function = prim::Constant[name="fallback_function", fallback=1]()
      %8 : (Tensor) = prim::CallFunction(%7, %bias.1, %input.1)
      %9 : Tensor = prim::TupleUnpack(%8)
      -> (%9)
  return (%5)
with prim::DifferentiableGraph_0 = graph(%0 : Tensor,
      %1 : Tensor):
  %2 : int = prim::Constant[value=1]()
  %5 : Tensor = aten::add(%1, %0, %2) # t.py:5:34
  %7 : int[] = aten::size(%1) # <string>:3:44
  %9 : int[] = aten::size(%5) # <string>:3:55
  %10 : int[]? = aten::_size_if_not_equal(%7, %9) # <string>:3:19
  %12 : int[] = aten::size(%0) # <string>:3:93
  %13 : int[]? = aten::_size_if_not_equal(%12, %9) # <string>:3:68
  %result.7 : Tensor = aten::relu(%5) # /opt/conda/lib/python3.6/site-packages/torch/nn/functional.py:1206:17
  return (%result.7, %10, %13, %result.7)