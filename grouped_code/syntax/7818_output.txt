graph(%x : Dynamic) {
  %output.1 : Long() = prim::Constant[value={0}]()
  %2 : Long() = prim::Constant[value={20}]()
  %3 : Byte() = prim::Constant[value={1}]()
  %output : Dynamic = prim::Loop(%2, %3, %output.1)
    block0(%i : Dynamic, %15 : Dynamic) {
      %5 : Long() = prim::Constant[value={0}]()
      %6 : Dynamic = aten::eq(%i, %5)
      %output.4 : Dynamic = prim::If(%6)
        block0() {
          %output.2 : Dynamic = aten::unsqueeze[dim=0](%x)
          -> (%output.2)
        }
        block1() {
          %10 : Dynamic = aten::unsqueeze[dim=0](%x)
          %12 : Long() = prim::Constant[value={0}]()
          %output.3 : Dynamic = aten::cat(%output.1, %10, %12)
          -> (%output.3)
        }
      %16 : Byte() = prim::Constant[value={1}]()
      -> (%16, %output.4)
    }
  return (%output);
}