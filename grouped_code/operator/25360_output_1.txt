Traceback (most recent call last):
  File "test.py", line 12, in <module>
    smod = th.jit.script(mod)
  File "/mnt/home/gbschwartz/anaconda/envs/py3_newpytorch_cuda10/lib/python3.7/site-packages/torch/jit/__init__.py", line 1161, in script
    return torch.jit.torch.jit._recursive.recursive_script(obj)                                                  
  File "/mnt/home/gbschwartz/anaconda/envs/py3_newpytorch_cuda10/lib/python3.7/site-packages/torch/jit/_recursive.py", line 133, in recursive_script
    stubs = list(map(make_stub, methods))
  File "/mnt/home/gbschwartz/anaconda/envs/py3_newpytorch_cuda10/lib/python3.7/site-packages/torch/jit/_recursive.py", line 131, in make_stub
    return torch.jit.script_method(func, _jit_internal.createResolutionCallbackFromClosure(func))                
  File "/mnt/home/gbschwartz/anaconda/envs/py3_newpytorch_cuda10/lib/python3.7/site-packages/torch/jit/__init__.py", line 1226, in script_method
    ast = get_jit_def(fn, self_name="ScriptModule")
  File "/mnt/home/gbschwartz/anaconda/envs/py3_newpytorch_cuda10/lib/python3.7/site-packages/torch/jit/frontend.py", line 166, in get_jit_def
    return build_def(ctx, py_ast.body[0], type_line, self_name)                                                  
  File "/mnt/home/gbschwartz/anaconda/envs/py3_newpytorch_cuda10/lib/python3.7/site-packages/torch/jit/frontend.py", line 206, in build_def
    build_stmts(ctx, body))
  File "/mnt/home/gbschwartz/anaconda/envs/py3_newpytorch_cuda10/lib/python3.7/site-packages/torch/jit/frontend.py", line 122, in build_stmts
    stmts = [build_stmt(ctx, s) for s in stmts]
  File "/mnt/home/gbschwartz/anaconda/envs/py3_newpytorch_cuda10/lib/python3.7/site-packages/torch/jit/frontend.py", line 122, in <listcomp>
    stmts = [build_stmt(ctx, s) for s in stmts]
  File "/mnt/home/gbschwartz/anaconda/envs/py3_newpytorch_cuda10/lib/python3.7/site-packages/torch/jit/frontend.py", line 182, in __call__
    return method(ctx, node)
  File "/mnt/home/gbschwartz/anaconda/envs/py3_newpytorch_cuda10/lib/python3.7/site-packages/torch/jit/frontend.py", line 298, in build_Return
    return Return(r, None if stmt.value is None else build_expr(ctx, stmt.value))                                
  File "/mnt/home/gbschwartz/anaconda/envs/py3_newpytorch_cuda10/lib/python3.7/site-packages/torch/jit/frontend.py", line 182, in __call__
    return method(ctx, node)
  File "/mnt/home/gbschwartz/anaconda/envs/py3_newpytorch_cuda10/lib/python3.7/site-packages/torch/jit/frontend.py", line 596, in build_Subscript
    return Subscript(base, [build_expr(ctx, expr.slice.value)])                                                  
  File "/mnt/home/gbschwartz/anaconda/envs/py3_newpytorch_cuda10/lib/python3.7/site-packages/torch/jit/frontend.py", line 182, in __call__
    return method(ctx, node)
  File "/mnt/home/gbschwartz/anaconda/envs/py3_newpytorch_cuda10/lib/python3.7/site-packages/torch/jit/frontend.py", line 503, in build_UnaryOp
    r = ctx.make_range(expr.lineno, expr.col_offset, expr.col_offset + len(op_token))                            
TypeError: object of type 'NoneType' has no len()