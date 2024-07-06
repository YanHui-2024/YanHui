python test-local-annotation2.py 
Traceback (most recent call last):
  File "test-local-annotation2.py", line 7, in <module>
    m = torch.jit.script(f)
  File "/home/pengwu/local/miniconda3/envs/pytorch/lib/python3.8/site-packages/torch/jit/_script.py", line 939, in script
    fn = torch._C._jit_script_compile(
RuntimeError: 
if-expression's true branch has type int but false branch has type float:
  File "test-local-annotation2.py", line 4
def f(a: int, b: float, flag: bool):
    value: Any = a if flag else b
                 ~~~~~~~~~~~~~~~~ <--- HERE
    return value