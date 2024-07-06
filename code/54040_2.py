graph(%0 : Tensor,
      %1 : Tensor,
      %self_size.5 : int[]?,
      %other_size.5 : int[]?,
      %result.7 : Tensor):
  %71 : int = prim::Constant[value=0]() # <string>:98:47
  %191 : None = prim::Constant()
  %192 : bool = aten::__is__(%self_size.5, %191)
  %193 : bool = prim::AutogradAllNonZero(%1, %result.7)
  %194 : bool = prim::AutogradAllZero(%0)
  %195 : bool[] = prim::ListConstruct(%192, %193, %194)
  %196 : bool = aten::all(%195)
  %63 : (Tensor, Tensor) = prim::If(%196)
    block0():
      %85 : Tensor = aten::gt(%result.7, %71) # <string>:98:38
      %88 : Tensor = aten::type_as(%85, %result.7) # <string>:98:38
      %91 : Tensor = aten::mul(%1, %88) # <string>:98:23
      %grad_other.7 : Tensor = aten::_grad_sum_to_size(%91, %other_size.5) # <string>:17:30
      %126 : (Tensor, Tensor) = prim::TupleConstruct(%grad_other.7, %91)
      -> (%126)
    block1():
      %198 : Function = prim::Constant[name="fallback_function", fallback=1]()
      %199 : ((Tensor, Tensor)) = prim::CallFunction(%198, %0, %1, %self_size.5, %other_size.5, %result.7)
      %200 : (Tensor, Tensor) = prim::TupleUnpack(%199)
      -> (%200)
  return (%63)