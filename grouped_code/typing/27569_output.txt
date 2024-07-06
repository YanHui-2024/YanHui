PyTorch version is 1.2.0
/usr/local/lib/python3.6/dist-packages/torch/onnx/utils.py:562: UserWarning: ONNX export failed on ATen operator dim because torch.onnx.symbolic_opset9.dim does not exist
  .format(op_name, opset_version, op_name))
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-1-036960002e79> in <module>()
     33                       example_outputs=dummy_output,
     34                       f=temp,
---> 35                       verbose=True)
 
7 frames
/usr/local/lib/python3.6/dist-packages/torch/onnx/__init__.py in export(model, args, f, export_params, verbose, training, input_names, output_names, aten, export_raw_ir, operator_export_type, opset_version, _retain_param_name, do_constant_folding, example_outputs, strip_doc_string, dynamic_axes)
    130                         operator_export_type, opset_version, _retain_param_name,
    131                         do_constant_folding, example_outputs,
--> 132                         strip_doc_string, dynamic_axes)
    133
    134
 
/usr/local/lib/python3.6/dist-packages/torch/onnx/utils.py in export(model, args, f, export_params, verbose, training, input_names, output_names, aten, export_raw_ir, operator_export_type, opset_version, _retain_param_name, do_constant_folding, example_outputs, strip_doc_string, dynamic_axes)
     62             operator_export_type=operator_export_type, opset_version=opset_version,
     63             _retain_param_name=_retain_param_name, do_constant_folding=do_constant_folding,
---> 64             example_outputs=example_outputs, strip_doc_string=strip_doc_string, dynamic_axes=dynamic_axes)
     65
     66
 
/usr/local/lib/python3.6/dist-packages/torch/onnx/utils.py in _export(model, args, f, export_params, verbose, training, input_names, output_names, operator_export_type, export_type, example_outputs, propagate, opset_version, _retain_param_name, do_constant_folding, strip_doc_string, dynamic_axes)
    327                                                         output_names, operator_export_type,
    328                                                         example_outputs, propagate,
--> 329                                                         _retain_param_name, do_constant_folding)
    330
    331         # TODO: Don't allocate a in-memory string for the protobuf
 
/usr/local/lib/python3.6/dist-packages/torch/onnx/utils.py in _model_to_graph(model, args, verbose, training, input_names, output_names, operator_export_type, example_outputs, propagate, _retain_param_name, do_constant_folding, _disable_torch_constant_prop)
    223
    224     graph = _optimize_graph(graph, operator_export_type,
--> 225                             _disable_torch_constant_prop=_disable_torch_constant_prop)
    226
    227     if isinstance(model, torch.jit.ScriptModule) or isinstance(model, torch.jit.Function):
 
/usr/local/lib/python3.6/dist-packages/torch/onnx/utils.py in _optimize_graph(graph, operator_export_type, _disable_torch_constant_prop)
    125         torch._C._jit_pass_erase_number_types(graph)
    126
--> 127         graph = torch._C._jit_pass_onnx(graph, operator_export_type)
    128         torch._C._jit_pass_lint(graph)
    129         from torch.onnx.symbolic_helper import _export_onnx_opset_version
 
/usr/local/lib/python3.6/dist-packages/torch/onnx/__init__.py in _run_symbolic_function(*args, **kwargs)
    161 def _run_symbolic_function(*args, **kwargs):
    162     from torch.onnx import utils
--> 163     return utils._run_symbolic_function(*args, **kwargs)
    164
    165
 
/usr/local/lib/python3.6/dist-packages/torch/onnx/utils.py in _run_symbolic_function(g, n, inputs, env, operator_export_type)
    561                                   "torch.onnx.symbolic_opset{}.{} does not exist"
    562                                   .format(op_name, opset_version, op_name))
--> 563                 op_fn = sym_registry.get_registered_op(op_name, '', opset_version)
    564                 return op_fn(g, *inputs, **attrs)
    565
 
/usr/local/lib/python3.6/dist-packages/torch/onnx/symbolic_registry.py in get_registered_op(opname, domain, version)
     89         warnings.warn("ONNX export failed. The ONNX domain and/or version are None.")
     90     global _registry
---> 91     return _registry[(domain, version)][opname]

KeyError: 'dim'