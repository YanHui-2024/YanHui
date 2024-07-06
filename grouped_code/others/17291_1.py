graph(%x : int):
  %3 : string = prim::Constant[value="Exception"]()
  %1 : int = prim::Constant[value=2]()
  %5 : int = prim::Constant[value=3]()
  %2 : bool = aten::gt(%x, %1)
   = prim::If(%2)
    block0():
       = prim::RaiseException(%3)
      -> ()
    block1():
      -> ()
  %6 : int = aten::add(%x, %5)
  return (%6)