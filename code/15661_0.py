import torch

def python_list_op(lst):
    # type: (List[Tensor]) -> Tensor
    return lst[0]

@torch.jit.script
def script_fn(lst):
    # type: (List[Tensor]) -> Tensor
    return python_list_op(lst)

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-4-81852451e4c4> in <module>()
      5     return lst[0]
      6
----> 7 @torch.jit.script
      8 def script_fn(lst):
      9     # type: (List[Tensor]) -> Tensor

/scratch/rzou/pt/master/torch/jit/__init__.py in script(fn, optimize, _frames_up, _rcb)
    691     ast = get_jit_ast(fn, is_method=False)
    692     mod = ScriptModule()
--> 693     _jit_script_compile(mod, ast, _rcb, get_default_args(fn))
    694     # Forward docstrings
    695     mod.__doc__ = fn.__doc__

/scratch/rzou/pt/master/torch/jit/annotations.py in get_signature(fn)
     50         return None
     51
---> 52     return parse_type_line(type_line)
     53
     54

/scratch/rzou/pt/master/torch/jit/annotations.py in parse_type_line(type_line)
     88
     89     try:
---> 90         arg_ann = eval(arg_ann_str, _eval_env)
     91     except SyntaxError:
     92         raise RuntimeError("Failed to parse the argument list of a type annotation")

<string> in <module>()

NameError: name 'List' is not defined