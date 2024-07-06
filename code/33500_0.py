      script::parseIR(
          R"IR(
  graph():
    %10 : bool = prim::Constant[value=0]()
    %8 : Device? = prim::Constant()
    %4 : int? = prim::Constant()
    %0 : int = prim::Constant[value=2]()
    %1 : int = prim::Constant[value=3]()
    %2 : int[] = prim::ListConstruct(%0, %1)
    %x : Tensor = aten::rand(%2, %4, %4, %8, %10)
    %12 : int[] = prim::ListConstruct(%0, %1)
    %y : Tensor = aten::rand(%12, %4, %4, %8, %10)
    %22 : int[] = prim::ListConstruct(%0, %1)
    %z : Tensor = aten::rand(%22, %4, %4, %8, %10)
    %32 : int[] = prim::ListConstruct(%0, %1)
    %fresh : Tensor = aten::rand(%32, %4, %4, %8, %10)
    %foo : Tensor[] = prim::ListConstruct(%x, %y)
    %43 : Tensor[] = aten::append(%foo, %z)
    return ()
  )IR",