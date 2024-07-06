graph(%view_20.1 : Float(10, 2, 96, strides=[192, 96, 1], requires_grad=0, device=cpu),
      %view_19.1 : Float(10, 2, 96, strides=[192, 96, 1], requires_grad=0, device=cpu),
      %view_18.1 : Float(10, 2, 96, strides=[192, 96, 1], requires_grad=0, device=cpu),
      %reshape.1 : Float(10, 38, 96, strides=[3648, 96, 1], requires_grad=0, device=cpu),
      %view_17.1 : Float(10, 2, 96, strides=[192, 96, 1], requires_grad=0, device=cpu)):
  %19 : int = prim::Constant[value=1]()
  %23 : Tensor[] = prim::ListConstruct(%reshape.1, %view_17.1)
  %cat_3.2 : Float(10, 40, 96, strides=[3840, 96, 1], requires_grad=0, device=cpu) = aten::cat(%23, %19)
  %17 : Tensor[] = prim::ListConstruct(%cat_3.2, %view_18.1)
  %cat_5.2 : Float(10, 42, 96, strides=[4032, 96, 1], requires_grad=0, device=cpu) = aten::cat(%17, %19)
  %11 : Tensor[] = prim::ListConstruct(%cat_5.2, %view_19.1)
  %cat_7.2 : Float(10, 44, 96, strides=[4224, 96, 1], requires_grad=0, device=cpu) = aten::cat(%11, %19) # <eval_with_key>.0:324:12
  %5 : Tensor[] = prim::ListConstruct(%cat_7.2, %view_20.1)
  %cat_9.2 : Float(10, 46, 96, strides=[4416, 96, 1], requires_grad=0, device=cpu) = aten::cat(%5, %19) # <eval_with_key>.0:343:12
  return (%cat_9.2)