%50 : int = prim::Constant[value=0](), scope: RNNTest
  %51 : int = aten::size(%15, %50), scope: RNNTest
  %52 : Long() = prim::NumToTensor(%51), scope: RNNTest