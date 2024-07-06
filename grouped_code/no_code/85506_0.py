Python 3.11.0b1 (main, Jul 28 2022, 09:24:40) [GCC 7.3.1 20180303 (Red Hat 7.3.1-5)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from functorch.dim import dims
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/root/pytorch/functorch/__init__.py", line 6, in <module>
    import torch
    ^^^^^^^^^^^^
  File "/root/pytorch/torch/__init__.py", line 917, in <module>
    os.environ.get('PYTORCH_DISABLE_LIBRARY', "0") == "0"):
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/pytorch/torch/_decomp/decompositions_for_jvp.py", line 287, in <module>
    _register_jit_decomposition_for_jvp(torch.ops.aten.nll_loss_backward.default)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/pytorch/torch/_decomp/decompositions_for_jvp.py", line 83, in _register_jit_decomposition_for_jvp
    graph = torch.jit.script(decomp_fn).graph
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/pytorch/torch/jit/_script.py", line 1343, in script
    fn = torch._C._jit_script_compile(
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/pytorch/torch/jit/annotations.py", line 386, in try_ann_to_type
    scripted_class = torch.jit._script._recursive_compile_class(ann, loc)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/pytorch/torch/jit/_script.py", line 1465, in _recursive_compile_class
    rcb = _jit_internal.createResolutionCallbackForClassMethods(obj)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/pytorch/torch/_jit_internal.py", line 454, in createResolutionCallbackForClassMethods
    captures.update(get_closure(fn))
                    ^^^^^^^^^^^^^^^
  File "/root/pytorch/torch/_jit_internal.py", line 206, in get_closure
    captures.update(fn.__globals__)
                    ^^^^^^^^^^^^^^
AttributeError: 'builtin_function_or_method' object has no attribute '__globals__'
>>> 