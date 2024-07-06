graph(%0 : Float(3, 4, 5, 6, 7),
      %1 : Float(3, 1, 1, 3, 2)):
  %2 : Float(3, 4, 5, 6, 7) = aten::clone(%0) # /home/work/anaconda3/envs/torch/lib/python3.7/site-packages/torch/jit/__init__.py:338:0
  %3 : Float(3, 1, 1, 3, 2) = aten::clone(%1) # /home/work/anaconda3/envs/torch/lib/python3.7/site-packages/torch/jit/__init__.py:338:0
  %4 : Long(3) = prim::Constant[value= 2  1  3 [ Variable[CPULongType]{3} ]](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %5 : Device = prim::Constant[value="cpu"](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %6 : int = prim::Constant[value=4](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %7 : bool = prim::Constant[value=0](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %8 : bool = prim::Constant[value=0](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %9 : Long(3) = aten::to(%4, %5, %6, %7, %8), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %10 : Long(3) = aten::detach(%9), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %11 : int = prim::Constant[value=4](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %12 : int = prim::Constant[value=2](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %13 : int = prim::Constant[value=4](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %14 : int = prim::Constant[value=1](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %15 : Float(3, 4, 5, 6, 2) = aten::slice(%0, %11, %12, %13, %14), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %16 : int = prim::Constant[value=4](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %17 : int = prim::Constant[value=0](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %18 : Device = prim::Constant[value="cpu"](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %19 : bool = prim::Constant[value=0](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %20 : bool = prim::Constant[value=0](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %21 : bool = prim::Constant[value=0](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %22 : Long(3) = aten::to(%10, %16, %17, %18, %19, %20, %21), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %23 : None = prim::Constant(), scope: IndexPutModel
  %24 : None = prim::Constant(), scope: IndexPutModel
  %25 : None = prim::Constant(), scope: IndexPutModel
  %26 : Tensor?[] = prim::ListConstruct(%23, %24, %25, %22), scope: IndexPutModel
  %27 : Float(3, 4, 5, 3, 2) = aten::index(%15, %26), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %28 : int = prim::Constant[value=1](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %29 : Float(3, 4, 5, 3, 2) = aten::add(%27, %1, %28), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %30 : int = prim::Constant[value=4](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %31 : int = prim::Constant[value=2](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %32 : int = prim::Constant[value=4](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %33 : int = prim::Constant[value=1](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %34 : Float(3, 4, 5, 6, 2) = aten::slice(%0, %30, %31, %32, %33), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %35 : int = prim::Constant[value=4](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %36 : int = prim::Constant[value=0](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %37 : Device = prim::Constant[value="cpu"](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %38 : bool = prim::Constant[value=0](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %39 : bool = prim::Constant[value=0](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %40 : bool = prim::Constant[value=0](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %41 : Long(3) = aten::to(%22, %35, %36, %37, %38, %39, %40), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %42 : None = prim::Constant(), scope: IndexPutModel
  %43 : None = prim::Constant(), scope: IndexPutModel
  %44 : None = prim::Constant(), scope: IndexPutModel
  %45 : Tensor?[] = prim::ListConstruct(%42, %43, %44, %41), scope: IndexPutModel
  %46 : bool = prim::Constant[value=0](), scope: IndexPutModel # repro_trace_inplace.py:5:0
  %47 : Float(3, 4, 5, 6, 2) = aten::index_put(%34, %45, %29, %46), scope: IndexPutModel # repro_trace_inplace.py:5:0
  return (%0)