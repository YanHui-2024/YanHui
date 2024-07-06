---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-10e6455dfe2d> in <module>
----> 1 torch.jit.trace(conv_m1, (x_m1,))

/opt/homebrew/lib/python3.9/site-packages/torch/jit/_trace.py in trace(func, example_inputs, optimize, check_trace, check_inputs, check_tolerance, strict, _force_outplace, _module_class, _compilation_unit)
    748
    749     if isinstance(func, torch.nn.Module):
--> 750         return trace_module(
    751             func,
    752             {"forward": example_inputs},

/opt/homebrew/lib/python3.9/site-packages/torch/jit/_trace.py in trace_module(mod, inputs, optimize, check_trace, check_inputs, check_tolerance, strict, _force_outplace, _module_class, _compilation_unit)
    990                     )
    991                 else:
--> 992                     _check_trace(
    993                         [inputs],
    994                         func,

/opt/homebrew/lib/python3.9/site-packages/torch/autograd/grad_mode.py in decorate_context(*args, **kwargs)
     25         def decorate_context(*args, **kwargs):
     26             with self.clone():
---> 27                 return func(*args, **kwargs)
     28         return cast(F, decorate_context)
     29

/opt/homebrew/lib/python3.9/site-packages/torch/jit/_trace.py in _check_trace(check_inputs, func, traced_func, check_tolerance, strict, force_outplace, is_trace_module, _module_class)
    525         traced_outs = run_mod_and_filter_tensor_outputs(traced_func, inputs, "trace")
    526         fn_outs = run_mod_and_filter_tensor_outputs(func, inputs, "Python function")
--> 527         if compare_outputs(traced_outs, fn_outs, "Python function"):
    528             check_outs = run_mod_and_filter_tensor_outputs(
    529                 check_mod_func, inputs, "repeated trace"

/opt/homebrew/lib/python3.9/site-packages/torch/jit/_trace.py in compare_outputs(original, reference, match_what)
    500                     else:
    501                         torch.testing.assert_close(
--> 502                             orig.double(),
    503                             ref.double(),
    504                             rtol=check_tolerance,

TypeError: Cannot convert a MPS Tensor to float64 dtype as the MPS framework doesn't support float64. Please use float32 instead.