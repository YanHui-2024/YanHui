Traceback (most recent call last):
  File "blah.py", line 21, in <module>
    model = torch.jit.script(model)
  File "/Users/michaelp/Code/Text-to-Speech/venv/lib/python3.7/site-packages/torch/jit/__init__.py", line 1162, in script
    return _convert_to_script_module(obj)
  File "/Users/michaelp/Code/Text-to-Speech/venv/lib/python3.7/site-packages/torch/jit/__init__.py", line 1811, in _convert_to_script_module
    stubs = list(map(make_stub, methods))
  File "/Users/michaelp/Code/Text-to-Speech/venv/lib/python3.7/site-packages/torch/jit/__init__.py", line 1809, in make_stub
    return script_method(func, _jit_internal.createResolutionCallbackFromClosure(func))
  File "/Users/michaelp/Code/Text-to-Speech/venv/lib/python3.7/site-packages/torch/jit/__init__.py", line 1204, in script_method
    ast = get_jit_def(fn, self_name="ScriptModule")
  File "/Users/michaelp/Code/Text-to-Speech/venv/lib/python3.7/site-packages/torch/jit/frontend.py", line 166, in get_jit_def
    return build_def(ctx, py_ast.body[0], type_line, self_name)
  File "/Users/michaelp/Code/Text-to-Speech/venv/lib/python3.7/site-packages/torch/jit/frontend.py", line 206, in build_def
    build_stmts(ctx, body))
  File "/Users/michaelp/Code/Text-to-Speech/venv/lib/python3.7/site-packages/torch/jit/frontend.py", line 122, in build_stmts
    stmts = [build_stmt(ctx, s) for s in stmts]
  File "/Users/michaelp/Code/Text-to-Speech/venv/lib/python3.7/site-packages/torch/jit/frontend.py", line 122, in <listcomp>
    stmts = [build_stmt(ctx, s) for s in stmts]
  File "/Users/michaelp/Code/Text-to-Speech/venv/lib/python3.7/site-packages/torch/jit/frontend.py", line 182, in __call__
    return method(ctx, node)
  File "/Users/michaelp/Code/Text-to-Speech/venv/lib/python3.7/site-packages/torch/jit/frontend.py", line 274, in build_Assign
    rhs = build_expr(ctx, stmt.value)
  File "/Users/michaelp/Code/Text-to-Speech/venv/lib/python3.7/site-packages/torch/jit/frontend.py", line 182, in __call__
    return method(ctx, node)
  File "/Users/michaelp/Code/Text-to-Speech/venv/lib/python3.7/site-packages/torch/jit/frontend.py", line 429, in build_Call
    func = build_expr(ctx, expr.func)
  File "/Users/michaelp/Code/Text-to-Speech/venv/lib/python3.7/site-packages/torch/jit/frontend.py", line 182, in __call__
    return method(ctx, node)
  File "/Users/michaelp/Code/Text-to-Speech/venv/lib/python3.7/site-packages/torch/jit/frontend.py", line 418, in build_Attribute
    pos = find_after(ctx, value.range().end, '.').end  # Start with the dot
  File "/Users/michaelp/Code/Text-to-Speech/venv/lib/python3.7/site-packages/torch/jit/frontend.py", line 678, in find_after
    new_pos = pos + ctx.source[pos:].index(substr)