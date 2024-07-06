(gdb) cout *graph
graph(%x : Float(2, 2)
      %y : Float(2, 2)
      %z : Float(4, 2)) {
  %3 : int = prim::Constant[value=1]()
  %y1 : Float(2, 2) = aten::sub(%x, %y, %3)
  %8 : int = prim::Constant[value=0]()
  %14 : Float(4, 2) = prim::FusionGroup_0[device=-1](%z, %y1, %x, %y)
  return (%14);
}
with prim::FusionGroup_0 = graph(%1 : Float(4, 2)
      %5 : Float(2, 2)
      %7 : Float(2, 2)
      %8 : Float(2, 2)) {
  %11 : int = prim::Constant[value=1]()
  %9 : int = prim::Constant[value=1]()
  %x1 : Float(2, 2) = aten::add(%7, %8, %9)
  %w : Float(4, 2) = prim::FusedConcat[dim=0](%x1, %5)
  %2 : int = prim::Constant[value=1]()
  %3 : Float(4, 2) = aten::add(%w, %1, %2)
  return (%3);
}