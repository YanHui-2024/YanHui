ERROR: Graphs differed across invocations!
        Graph diff:
                  graph(%self.1 : __torch__.MyModule,
                        %x : Tensor):
                    %cv1 : __torch__.torch.nn.modules.conv.Conv2d = prim::GetAttr[name="cv1"](%self.1)
                    %4 : int = prim::Constant[value=15]()
                    %5 : bool = prim::Constant[value=1](), scope: __module.cv1 # /home/titaiwang/pytorch/torch/nn/modules/conv.py:459:0
                    %6 : int = prim::Constant[value=0](), scope: __module.cv1 # /home/titaiwang/pytorch/torch/nn/modules/conv.py:459:0
                    %7 : int = prim::Constant[value=1](), scope: __module.cv1 # /home/titaiwang/pytorch/torch/nn/modules/conv.py:459:0
                    %8 : int = prim::Constant[value=2](), scope: __module.cv1 # /home/titaiwang/pytorch/torch/nn/modules/conv.py:459:0
                +   %9 : Tensor = prim::Constant[value=0.01 *  6.7810  6.4636  5.3894 [ CUDAHalfType{3} ]](), scope: __module.cv1 # /home/titaiwang/pytorch/torch/nn/modules/conv.py:459:0
                +   %10 : Tensor = prim::Constant[value=<Tensor>](), scope: __module.cv1 # /home/titaiwang/pytorch/torch/nn/modules/conv.py:459:0
                -   %9 : NoneType = prim::Constant(), scope: __module.cv1
                ?    ^
                +   %11 : NoneType = prim::Constant(), scope: __module.cv1
                ?    ^^
                -   %10 : bool = prim::Constant[value=0](), scope: __module.cv1 # /home/titaiwang/pytorch/torch/nn/modules/conv.py:459:0
                ?     ^
                +   %12 : bool = prim::Constant[value=0](), scope: __module.cv1 # /home/titaiwang/pytorch/torch/nn/modules/conv.py:459:0
                ?     ^
                -   %11 : int = prim::Constant[value=5](), scope: __module.cv1 # /home/titaiwang/pytorch/torch/nn/modules/conv.py:459:0
                ?     ^
                +   %13 : int = prim::Constant[value=5](), scope: __module.cv1 # /home/titaiwang/pytorch/torch/nn/modules/conv.py:459:0
                ?     ^
                -   %weight : Tensor = prim::GetAttr[name="weight"](%cv1)
                -   %bias : Tensor = prim::GetAttr[name="bias"](%cv1)
                -   %14 : Tensor = aten::to(%bias, %11, %10, %10, %9), scope: __module.cv1 # /home/titaiwang/pytorch/torch/nn/modules/conv.py:459:0
                -   %15 : Tensor = aten::to(%weight, %11, %10, %10, %9), scope: __module.cv1 # /home/titaiwang/pytorch/torch/nn/modules/conv.py:459:0
                -   %16 : Tensor = aten::to(%x, %11, %10, %10, %9), scope: __module.cv1 # /home/titaiwang/pytorch/torch/nn/modules/conv.py:459:0
                ?     ^                            --------------
                +   %14 : Tensor = aten::to(%x, %13, %12, %12, %11), scope: __module.cv1 # /home/titaiwang/pytorch/torch/nn/modules/conv.py:459:0
                ?     ^                         +++++++++++++++
                -   %17 : int[] = prim::ListConstruct(%8, %8), scope: __module.cv1
                ?     ^
                +   %15 : int[] = prim::ListConstruct(%8, %8), scope: __module.cv1
                ?     ^
                -   %18 : int[] = prim::ListConstruct(%7, %7), scope: __module.cv1
                ?     ^
                +   %16 : int[] = prim::ListConstruct(%7, %7), scope: __module.cv1
                ?     ^
                -   %19 : int[] = prim::ListConstruct(%7, %7), scope: __module.cv1
                ?     ^
                +   %17 : int[] = prim::ListConstruct(%7, %7), scope: __module.cv1
                ?     ^
                -   %20 : int[] = prim::ListConstruct(%6, %6), scope: __module.cv1
                ?    ^^
                +   %18 : int[] = prim::ListConstruct(%6, %6), scope: __module.cv1
                ?    ^^
                +   %19 : Tensor = aten::_autocast_to_reduced_precision(%14, %5, %12, %13, %4)
                +   %20 : Tensor = aten::_autocast_to_reduced_precision(%10, %5, %12, %13, %4)
                -   %21 : Tensor = aten::_autocast_to_reduced_precision(%16, %5, %10, %11, %4)
                ?                                                        ^^        ^    ^
                +   %21 : Tensor = aten::_autocast_to_reduced_precision(%9, %5, %12, %13, %4)
                ?                                                        ^        ^    ^
                -   %22 : Tensor = aten::_autocast_to_reduced_precision(%15, %5, %10, %11, %4)
                -   %23 : Tensor = aten::_autocast_to_reduced_precision(%14, %5, %10, %11, %4)
                -   %24 : Tensor = aten::_convolution(%21, %22, %23, %17, %18, %19, %10, %20, %7, %10, %10, %5, %5), scope: __module.cv1 # /home/titaiwang/pytorch/torch/nn/modules/conv.py:459:0
                ?     ^                                     ^^   ^^            ---------------      ^    ^
                +   %22 : Tensor = aten::_convolution(%19, %20, %21, %15, %16, %17, %12, %18, %7, %12, %12, %5, %5), scope: __module.cv1 # /home/titaiwang/pytorch/torch/nn/modules/conv.py:459:0
                ?     ^                                ++++++++++     ^^   ^^       +++++           ^    ^
                -   return (%24)
                ?             ^
                +   return (%22)
                ?             ^
        First diverging operator:
        Node diff:
                - %cv1 : __torch__.torch.nn.modules.conv.___torch_mangle_2.Conv2d = prim::GetAttr[name="cv1"](%self.1)
                ?                                                        ^
                + %cv1 : __torch__.torch.nn.modules.conv.___torch_mangle_4.Conv2d = prim::GetAttr[name="cv1"](%self.1)
                ?                                                        ^