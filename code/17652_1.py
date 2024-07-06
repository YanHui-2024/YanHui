Traceback (most recent call last):
  File "test.py", line 3, in <module>
    @torch.jit.script
  File "/home/gaoxiang/.virtualenvs/pt/lib/python3.7/site-packages/torch/jit/__init__.py", line 734, in script
    _jit_script_compile(mod, ast, _rcb, get_default_args(obj))
RuntimeError: 
arguments for call are not valid:
  
  for operator aten::eq(Tensor self, Tensor other) -> Tensor:
  expected a value of type Tensor for argument 'self' but found Scalar
  @torch.jit.script
  def f(a):
      return a[0].item() == 1
             ~~~~~~~~~ <--- HERE
  
  for operator aten::eq(Tensor self, Scalar other) -> Tensor:
  expected a value of type Tensor for argument 'self' but found Scalar
  @torch.jit.script
  def f(a):
      return a[0].item() == 1
             ~~~~~~~~~ <--- HERE
  
  for operator aten::eq(Tensor self, Tensor other, *, Tensor out) -> Tensor:
  expected a value of type Tensor for argument 'self' but found Scalar
  @torch.jit.script
  def f(a):
      return a[0].item() == 1
             ~~~~~~~~~ <--- HERE
  
  for operator aten::eq(Tensor self, Scalar other, *, Tensor out) -> Tensor:
  expected a value of type Tensor for argument 'self' but found Scalar
  @torch.jit.script
  def f(a):
      return a[0].item() == 1
             ~~~~~~~~~ <--- HERE
  
  for operator aten::eq(Device a, Device b) -> bool:
  expected a value of type Device for argument 'a' but found Scalar
  @torch.jit.script
  def f(a):
      return a[0].item() == 1
             ~~~~~~~~~ <--- HERE
  
  for operator aten::eq(string a, string b) -> bool:
  expected a value of type string for argument 'a' but found Scalar
  @torch.jit.script
  def f(a):
      return a[0].item() == 1
             ~~~~~~~~~ <--- HERE
  
  for operator aten::eq(int[] a, int[] b) -> bool:
  expected a value of type int[] for argument 'a' but found Scalar
  @torch.jit.script
  def f(a):
      return a[0].item() == 1
             ~~~~~~~~~ <--- HERE
  
  for operator aten::eq(float[] a, float[] b) -> bool:
  expected a value of type float[] for argument 'a' but found Scalar
  @torch.jit.script
  def f(a):
      return a[0].item() == 1
             ~~~~~~~~~ <--- HERE
  
  for operator aten::eq(Tensor[] a, Tensor[] b) -> bool:
  expected a value of type Tensor[] for argument 'a' but found Scalar
  @torch.jit.script
  def f(a):
      return a[0].item() == 1
             ~~~~~~~~~ <--- HERE
  
  for operator aten::eq(bool[] a, bool[] b) -> bool:
  expected a value of type bool[] for argument 'a' but found Scalar
  @torch.jit.script
  def f(a):
      return a[0].item() == 1
             ~~~~~~~~~ <--- HERE
  
  for operator aten::eq(int a, int b) -> bool:
  expected a value of type int for argument 'a' but found Scalar
  @torch.jit.script
  def f(a):
      return a[0].item() == 1
             ~~~~~~~~~ <--- HERE
  
  for operator aten::eq(float a, float b) -> bool:
  expected a value of type float for argument 'a' but found Scalar
  @torch.jit.script
  def f(a):
      return a[0].item() == 1
             ~~~~~~~~~ <--- HERE
  
  for operator aten::eq(int a, float b) -> bool:
  expected a value of type int for argument 'a' but found Scalar
  @torch.jit.script
  def f(a):
      return a[0].item() == 1
             ~~~~~~~~~ <--- HERE
  
  for operator aten::eq(float a, int b) -> bool:
  expected a value of type float for argument 'a' but found Scalar
  @torch.jit.script
  def f(a):
      return a[0].item() == 1
             ~~~~~~~~~ <--- HERE
  
  for operator eq(float a, Tensor b) -> Tensor:
  expected a value of type float for argument 'a' but found Scalar
  @torch.jit.script
  def f(a):
      return a[0].item() == 1
             ~~~~~~~~~ <--- HERE
  
  for operator eq(int a, Tensor b) -> Tensor:
  expected a value of type int for argument 'a' but found Scalar
  @torch.jit.script
  def f(a):
      return a[0].item() == 1
             ~~~~~~~~~ <--- HERE
for call at:
@torch.jit.script
def f(a):
    return a[0].item() == 1
           ~~~~~~~~~~~~~~~~ <--- HERE