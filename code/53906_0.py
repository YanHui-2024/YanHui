_________________________________________________________________________________ TestCommonCPU.test_variant_consistency_jit_stack_cpu_float64 __________________________________________________________________________________

self = <test_ops.TestCommonCPU testMethod=test_variant_consistency_jit_stack_cpu_float64>, device = 'cpu', dtype = torch.float64, op = <torch.testing._internal.common_methods_invocations.OpInfo object at 0x7f7b6e345460>

    @ops(op_db)
    def test_variant_consistency_jit(self, device, dtype, op):
        test_backward = op.supports_autograd and (
            (dtype.is_complex and op.test_complex_grad) or
            (dtype.is_floating_point and (not op.skip_bfloat16_grad or dtype != torch.bfloat16)))
    
        samples = op.sample_inputs(device, dtype, requires_grad=test_backward)
        if len(samples) == 0:
            self.skipTest("Skipped! No sample inputs!")
    
        for sample in samples:
    
            # Acquires variants to test
            func = op.get_op()
            method = op.get_method()
            inplace = op.get_inplace()
            variants = {
                'function': func, 'method': method,
                # TODO: inplace tests currently fail
                # 'inplace': inplace,
            }
    
            # Test traced and scripted consistency
            for func_type, variant in variants.items():
                if variant is None:
                    continue
    
                # Create accessor for script function variant
                name = op.name + '_' if func_type == 'inplace' else op.name
    
                # run with disable_autodiff_subgraph_inlining(True) to test
                #   autodiff support. Context manager forces the graph to contain
                #   DifferentiableGraph nodes if they are present
                with disable_autodiff_subgraph_inlining():
    
                    # Check scripted forward, grad, and grad grad
                    script_fn = create_script_fn(self, name, func_type)
>                   check_against_reference(self,
                                            script_fn,
                                            func,
                                            lambda x: x,
                                            (*sample.input,) + sample.args,
                                            sample.kwargs,
                                            no_grad=not test_backward)

test/test_ops.py:299: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
torch/testing/_internal/common_jit.py:63: in check_against_reference
    outputs_test = self.runAndSaveRNG(func, nograd_inputs, kwargs)
torch/testing/_internal/common_jit.py:130: in runAndSaveRNG
    results = func(*inputs, **kwargs)
torch/testing/_internal/jit_metaprogramming_utils.py:301: in script_fn
    fn, tensors = gen_script_fn_and_args(method_name, func_type, *args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

method_name = 'stack', func_type = 'function'
args = ((tensor([[-4.8270, -7.5824, -0.6047, -1.5412, -1.9719],
        [-4.1460, -5.4215, -4.7842, -4.1508,  7.3808],
      ...,  8.5671, -6.3773,  6.0237, -0.1426],
        [-0.0862,  5.3611,  7.2619, -1.8770, -1.0867]], requires_grad=True)), 0)
kwargs = {}, formals = [], tensors = []
actuals = ['(tensor([[-4.8270, -7.5824, -0.6047, -1.5412, -1.9719],\n        [-4.1460, -5.4215, -4.7842, -4.1508,  7.3808],\n   ....5671, -6.3773,  6.0237, -0.1426],\n        [-0.0862,  5.3611,  7.2619, -1.8770, -1.0867]], requires_grad=True))', '0']
call = 'torch.stack((tensor([[-4.8270, -7.5824, -0.6047, -1.5412, -1.9719],\n        [-4.1460, -5.4215, -4.7842, -4.1508,  7.... 8.5671, -6.3773,  6.0237, -0.1426],\n        [-0.0862,  5.3611,  7.2619, -1.8770, -1.0867]], requires_grad=True)), 0)'
script = '\ndef the_method():\n    return torch.stack((tensor([[-4.8270, -7.5824, -0.6047, -1.5412, -1.9719],\n        [-4.1460....5671, -6.3773,  6.0237, -0.1426],\n        [-0.0862,  5.3611,  7.2619, -1.8770, -1.0867]], requires_grad=True)), 0)\n'

    def gen_script_fn_and_args(method_name, func_type, *args, **kwargs):
        formals, tensors, actuals = get_script_args(args)
        call = get_call(method_name, func_type, actuals, kwargs)
        script = script_template.format(', '.join(formals), call)
>       CU = torch.jit.CompilationUnit(script)
E       RuntimeError: 
E       undefined value tensor:
E         File "<string>", line 3
E       
E       def the_method():
E           return torch.stack((tensor([[-4.8270, -7.5824, -0.6047, -1.5412, -1.9719],
E                               ~~~~~~ <--- HERE
E               [-4.1460, -5.4215, -4.7842, -4.1508,  7.3808],
E               [ 5.5761, -8.3157,  4.1776,  2.0474, -4.0760],

torch/testing/_internal/jit_metaprogramming_utils.py:292: RuntimeError