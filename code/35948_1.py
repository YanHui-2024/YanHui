  File "C:\Miniconda3\lib\site-packages\torch\jit\__init__.py", line 1281, in script
    fn = torch._C._jit_script_compile(qualified_name, ast, _rcb, get_default_args(obj))
RuntimeError: 
Arguments for call are not valid.
The following variants are available:
  
  aten::Int(Tensor a) -> (int):
  Expected a value of type 'Tensor' for argument 'a' but instead found type 'str'.
  
  aten::Int(bool a) -> (int):
  Expected a value of type 'bool' for argument 'a' but instead found type 'str'.
  
  aten::Int(float a) -> (int):
  Expected a value of type 'float' for argument 'a' but instead found type 'str'.
  
  aten::Int(Scalar a) -> (int):
  Expected a value of type 'number' for argument 'a' but instead found type 'str'.

The original call is:
  File "D:/GitHub/yolov3/qwe.py", line 6
def f(s: str):
    return int(s)
           ~~~ <--- HERE