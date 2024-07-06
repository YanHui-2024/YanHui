---short:
def forward(self,
    arg: List[Tensor]) -> List[Tuple[Tensor]]:
  _0 = [(arg[1],), (torch.argmax(arg[0], None, False),)]
  return _0

graph(%self : __torch__.___torch_mangle_0.OrderModuleShort,
      %arg.1 : Tensor[]):
  %10 : bool = prim::Constant[value=0]()
  %9 : None = prim::Constant()
  %3 : int = prim::Constant[value=1]() # <ipython-input-2-e60618fa51db>:9:21
  %7 : int = prim::Constant[value=0]() # <ipython-input-2-e60618fa51db>:9:32
  %4 : Tensor = aten::__getitem__(%arg.1, %3) # <ipython-input-2-e60618fa51db>:9:17
  %5 : (Tensor) = prim::TupleConstruct(%4)
  %8 : Tensor = aten::__getitem__(%arg.1, %7) # <ipython-input-2-e60618fa51db>:9:28
  %11 : Tensor = aten::argmax(%8, %9, %10) # <ipython-input-2-e60618fa51db>:9:28
  %12 : (Tensor) = prim::TupleConstruct(%11)
  %13 : (Tensor)[] = prim::ListConstruct(%5, %12)
  return (%13)


original
list index out of range

scripted
The following operation failed in the TorchScript interpreter.
Traceback of TorchScript (most recent call last):
  File "<ipython-input-2-e60618fa51db>", line 9, in forward
    def forward(self, arg: List[torch.Tensor]):
        return [(arg[1],), (arg[0].argmax(),)]
                 ~~~~~ <--- HERE
RuntimeError: list index out of range


loaded
The following operation failed in the TorchScript interpreter.
Traceback of TorchScript, serialized code (most recent call last):
  File "code/__torch__/___torch_mangle_0.py", line 6, in forward
  def forward(self: __torch__.___torch_mangle_0.OrderModuleShort,
    arg: List[Tensor]) -> List[Tuple[Tensor]]:
    _0 = (arg[1],)
          ~~~~~ <--- HERE
    _1 = (torch.argmax(arg[0], None, False),)
    return [_0, _1]

Traceback of TorchScript, original code (most recent call last):
  File "<ipython-input-2-e60618fa51db>", line 9, in forward
    def forward(self, arg: List[torch.Tensor]):
        return [(arg[1],), (arg[0].argmax(),)]
                 ~~~~~ <--- HERE
RuntimeError: list index out of range


---long:
def forward(self,
    long_arg_name: List[Tensor]) -> List[Tuple[Tensor]]:
  _0 = torch.argmax(long_arg_name[0], None, False)
  return [(long_arg_name[1],), (_0,)]

graph(%self : __torch__.___torch_mangle_1.OrderModuleLong,
      %long_arg_name.1 : Tensor[]):
  %10 : bool = prim::Constant[value=0]()
  %9 : None = prim::Constant()
  %3 : int = prim::Constant[value=1]() # <ipython-input-2-e60618fa51db>:13:31
  %7 : int = prim::Constant[value=0]() # <ipython-input-2-e60618fa51db>:13:52
  %4 : Tensor = aten::__getitem__(%long_arg_name.1, %3) # <ipython-input-2-e60618fa51db>:13:17
  %5 : (Tensor) = prim::TupleConstruct(%4)
  %8 : Tensor = aten::__getitem__(%long_arg_name.1, %7) # <ipython-input-2-e60618fa51db>:13:38
  %11 : Tensor = aten::argmax(%8, %9, %10) # <ipython-input-2-e60618fa51db>:13:38
  %12 : (Tensor) = prim::TupleConstruct(%11)
  %13 : (Tensor)[] = prim::ListConstruct(%5, %12)
  return (%13)


original
list index out of range

scripted
The following operation failed in the TorchScript interpreter.
Traceback of TorchScript (most recent call last):
  File "<ipython-input-2-e60618fa51db>", line 13, in forward
    def forward(self, long_arg_name: List[torch.Tensor]):
        return [(long_arg_name[1],), (long_arg_name[0].argmax(),)]
                 ~~~~~~~~~~~~~~~ <--- HERE
RuntimeError: list index out of range


loaded
The following operation failed in the TorchScript interpreter.
Traceback of TorchScript, serialized code (most recent call last):
  File "code/__torch__/___torch_mangle_1.py", line 6, in forward
  def forward(self: __torch__.___torch_mangle_1.OrderModuleLong,
    long_arg_name: List[Tensor]) -> List[Tuple[Tensor]]:
    _0 = torch.argmax(long_arg_name[0], None, False)
         ~~~~~~~~~~~~ <--- HERE
    return [(long_arg_name[1],), (_0,)]

Traceback of TorchScript, original code (most recent call last):
  File "<ipython-input-2-e60618fa51db>", line 13, in forward
    def forward(self, long_arg_name: List[torch.Tensor]):
        return [(long_arg_name[1],), (long_arg_name[0].argmax(),)]
                                      ~~~~~~~~~~~~~~~~~~~~~~ <--- HERE
RuntimeError: cannot perform reduction function argmax on a tensor with no elements because the operation does not have an identity