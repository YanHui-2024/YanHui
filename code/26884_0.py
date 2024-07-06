tamas@super-duper-compute-machine:~/JUPYTER_LAB$ ipython
Python 3.7.3 (default, Mar 27 2019, 22:11:17) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.6.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import torch                                                                                                                              

In [2]: torch.__version__                                                                                                                         
Out[2]: '1.2.0'

In [3]: class MyCell(torch.nn.Module): 
   ...:     def __init__(self): 
   ...:         super(MyCell, self).__init__() 
   ...:         self.linear = torch.nn.Linear(4, 4) 
   ...:  
   ...:     def forward(self, x, h): 
   ...:         new_h = torch.tanh(self.linear(x) + h) 
   ...:         return new_h, new_h 
   ...:  
   ...: model = MyCell() 
   ...: x, h = torch.rand(3, 4), torch.rand(3, 4) 
   ...: scripted_model = torch.jit.script(model, (x, h))                                                                                          
/home/tamas/anaconda3/envs/cuda/lib/python3.7/site-packages/torch/jit/__init__.py:1158: UserWarning: `optimize` is deprecated and has no effect. Use `with torch.jit.optimized_execution() instead
  warnings.warn("`optimize` is deprecated and has no effect. Use `with torch.jit.optimized_execution() instead")

In [4]: scripted_model.code                                                                                                                       
Out[4]: 'def forward(self,\n    x: Tensor,\n    h: Tensor) -> Tuple[Tensor, Tensor]:\n  _0 = self.linear\n  _1 = _0.weight\n  _2 = _0.bias\n  if torch.eq(torch.dim(x), 2):\n    _3 = torch.__isnot__(_2, None)\n  else:\n    _3 = False\n  if _3:\n    bias = ops.prim.unchecked_unwrap_optional(_2)\n    ret = torch.addmm(bias, x, torch.t(_1), beta=1, alpha=1)\n  else:\n    output = torch.matmul(x, torch.t(_1))\n    if torch.__isnot__(_2, None):\n      bias0 = ops.prim.unchecked_unwrap_optional(_2)\n      output0 = torch.add_(output, bias0, alpha=1)\n    else:\n      output0 = output\n    ret = output0\n  new_h = torch.tanh(torch.add(ret, h, alpha=1))\n  return (new_h, new_h)\n'

In [5]: scripted_model.training                                                                                                                   
Out[5]: True

In [6]: scripted_model.eval()                                                                                                                     
Out[6]: 
WeakScriptModuleProxy(
  (linear): WeakScriptModuleProxy()
)

In [7]: scripted_model.training                                                                                                                   
Out[7]: False

In [8]: torch.jit.save(scripted_model, 'temp.pt')                                                                                                 

In [9]: m = torch.jit.load('temp.pt')                                                                                                             

In [10]: m.training                                                                                                                               
Out[10]: True