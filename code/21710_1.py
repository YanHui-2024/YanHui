Traceback (most recent call last):
  File "./test.py", line 3, in <module>
    def foo(x):
  File "/Users/btv/pysandbox/lib/python3.8/site-packages/torch/jit/__init__.py", line 1079, in script
    ast = get_jit_def(obj)
  File "/Users/btv/pysandbox/lib/python3.8/site-packages/torch/jit/frontend.py", line 169, in get_jit_def
    return build_def(ctx, py_ast.body[0], type_line, self_name)
  File "/Users/btv/pysandbox/lib/python3.8/site-packages/torch/jit/frontend.py", line 209, in build_def
    build_stmts(ctx, body))
  File "/Users/btv/pysandbox/lib/python3.8/site-packages/torch/jit/frontend.py", line 125, in build_stmts
    stmts = [build_stmt(ctx, s) for s in stmts]
  File "/Users/btv/pysandbox/lib/python3.8/site-packages/torch/jit/frontend.py", line 125, in <listcomp>
    stmts = [build_stmt(ctx, s) for s in stmts]
  File "/Users/btv/pysandbox/lib/python3.8/site-packages/torch/jit/frontend.py", line 185, in __call__
    return method(ctx, node)
  File "/Users/btv/pysandbox/lib/python3.8/site-packages/torch/jit/frontend.py", line 288, in build_Return
    return Return(r, None if stmt.value is None else build_expr(ctx, stmt.value))
  File "/Users/btv/pysandbox/lib/python3.8/site-packages/torch/jit/frontend.py", line 185, in __call__
    return method(ctx, node)
  File "/Users/btv/pysandbox/lib/python3.8/site-packages/torch/jit/frontend.py", line 422, in build_Call
    kw_expr = build_expr(ctx, kw.value)
  File "/Users/btv/pysandbox/lib/python3.8/site-packages/torch/jit/frontend.py", line 184, in __call__
    raise UnsupportedNodeError(ctx, node)
torch.jit.frontend.UnsupportedNodeError: Constant aren't supported
at ./test.py:4:29
@torch.jit.script
def foo(x):
    return torch.sum(x, dim=1)
                            ~ <--- HERE