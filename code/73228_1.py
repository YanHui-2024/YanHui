tensor(2.+6.j, device='cuda:0')
(2+6j)
graph(%x.1 : complex,
      %y.1 : Tensor):
  %6 : int = prim::Constant[value=2]() # /home/gaoxiang/misc/jit_complex_scalar.py:5:8
  %4 : complex = aten::ComplexImplicit(%y.1) # /home/gaoxiang/misc/jit_complex_scalar.py:4:8
  %o.1 : complex = aten::add(%x.1, %4) # /home/gaoxiang/misc/jit_complex_scalar.py:4:8
  %o.5 : complex = aten::add(%6, %o.1) # /home/gaoxiang/misc/jit_complex_scalar.py:5:8
  return (%o.5)

graph(%x.1 : complex,
      %y.1 : Tensor):
  %2 : int = prim::Constant[value=2]() # /home/gaoxiang/misc/jit_complex_scalar.py:5:8
  %3 : complex = aten::ComplexImplicit(%y.1) # /home/gaoxiang/misc/jit_complex_scalar.py:4:8
  %o.1 : complex = aten::add(%x.1, %3) # /home/gaoxiang/misc/jit_complex_scalar.py:4:8
  %o.5 : complex = aten::add(%2, %o.1) # /home/gaoxiang/misc/jit_complex_scalar.py:5:8
  return (%o.5)