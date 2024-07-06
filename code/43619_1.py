Original module
Correct

Traced module
forward() is missing value for argument 'x'. Declaration: forward(__torch__.___torch_mangle_61.AnotherTestModule self, Tensor x) -> (Tensor) 

Traced module code
def forward(self,
    x: Tensor) -> Tensor:
  return (self.inner_module).forward(x, )