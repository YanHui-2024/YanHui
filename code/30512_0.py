Traceback (most recent call last):
  File "/home/liron/envs/detectron/lib/python3.6/site-packages/torch/onnx/utils.py", line 382, in _export
    fixed_batch_size=fixed_batch_size)
  File "/home/liron/envs/detectron/lib/python3.6/site-packages/torch/onnx/utils.py", line 262, in _model_to_graph
    fixed_batch_size=fixed_batch_size)
  File "/home/liron/envs/detectron/lib/python3.6/site-packages/torch/onnx/utils.py", line 132, in _optimize_graph
    graph = torch._C._jit_pass_onnx(graph, operator_export_type)
  File "/home/liron/envs/detectron/lib/python3.6/site-packages/torch/onnx/__init__.py", line 174, in _run_symbolic_function
    return utils._run_symbolic_function(*args, **kwargs)
  File "/home/liron/envs/detectron/lib/python3.6/site-packages/torch/onnx/utils.py", line 619, in _run_symbolic_function
    return op_fn(g, *inputs, **attrs)
  File "/home/liron/envs/detectron/lib/python3.6/site-packages/torch/onnx/symbolic_helper.py", line 124, in wrapper
    return fn(g, *args)
  File "/home/liron/envs/detectron/lib/python3.6/site-packages/torch/onnx/symbolic_opset9.py", line 862, in batch_norm
    if len(input_sizes) == 2:
TypeError: object of type 'NoneType' has no len() (occurred when translating batch_norm)