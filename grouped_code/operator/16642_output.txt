no jit tensor(5.0859, device='cuda:0', dtype=torch.float16)
Traceback (most recent call last):
  File "fused_bn.py", line 35, in <module>
    test_fuse_batch_norm()
  File "fused_bn.py", line 30, in test_fuse_batch_norm
    out_opt = model(x,y)
  File "/workspace/ALL/pytorch_upstream/torch/nn/modules/module.py", line 492, in __call__
    result = self.forward(*input, **kwargs)
RuntimeError: 
expected scalar type Half but found Float (data<c10::Half> at /workspace/ALL/pytorch_upstream/aten/src/ATen/core/TensorMethods.h:1314)
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x6a (0x7f9332568f2a in /workspace/ALL/pytorch_upstream/torch/lib/libc10.so)
frame #1: <unknown function> + 0x1e7d826 (0x7f933770a826 in /workspace/ALL/pytorch_upstream/torch/lib/libcaffe2_gpu.so)
frame #2: <unknown function> + 0x2104fe9 (0x7f9337991fe9 in /workspace/ALL/pytorch_upstream/torch/lib/libcaffe2_gpu.so)
frame #3: std::tuple<at::Tensor, at::Tensor> at::native::batch_norm_update_stats_cuda_template<c10::Half, int>(at::Tensor const&, at::Tensor const&, at::Tensor const&, double) + 0x1af (0x7f93379a046f in /workspace/ALL/pytorch_upstream/torch/lib/libcaffe2_gpu.so)
frame #4: at::native::batch_norm_update_stats_cuda(at::Tensor const&, at::Tensor const&, at::Tensor const&, double) + 0x4e5 (0x7f9337992e65 in /workspace/ALL/pytorch_upstream/torch/lib/libcaffe2_gpu.so)
frame #5: at::CUDAHalfType::batch_norm_update_stats(at::Tensor const&, at::Tensor const&, at::Tensor const&, double) const + 0x9d (0x7f933812777d in /workspace/ALL/pytorch_upstream/torch/lib/libcaffe2_gpu.so)
frame #6: torch::autograd::VariableType::batch_norm_update_stats(at::Tensor const&, at::Tensor const&, at::Tensor const&, double) const + 0x271 (0x7f9331a2fca1 in /workspace/ALL/pytorch_upstream/torch/lib/libtorch.so.1)
frame #7: <unknown function> + 0x5400fe (0x7f9331c4c0fe in /workspace/ALL/pytorch_upstream/torch/lib/libtorch.so.1)
frame #8: <unknown function> + 0x62f1ed (0x7f9331d3b1ed in /workspace/ALL/pytorch_upstream/torch/lib/libtorch.so.1)
frame #9: torch::jit::InterpreterState::run(std::vector<c10::IValue, std::allocator<c10::IValue> >&) + 0x31 (0x7f9331d36451 in /workspace/ALL/pytorch_upstream/torch/lib/libtorch.so.1)
frame #10: torch::jit::GraphExecutor::run(std::vector<c10::IValue, std::allocator<c10::IValue> >&) + 0x1da (0x7f9331d17cfa in /workspace/ALL/pytorch_upstream/torch/lib/libtorch.so.1)
frame #11: <unknown function> + 0x3dcbfd (0x7f93496debfd in /workspace/ALL/pytorch_upstream/torch/lib/libtorch_python.so)
frame #12: <unknown function> + 0x3b8c86 (0x7f93496bac86 in /workspace/ALL/pytorch_upstream/torch/lib/libtorch_python.so)
frame #13: <unknown function> + 0x10ad8d (0x7f934940cd8d in /workspace/ALL/pytorch_upstream/torch/lib/libtorch_python.so)
<omitting python frames>
frame #39: __libc_start_main + 0xf0 (0x7f935acf1830 in /lib/x86_64-linux-gnu/libc.so.6)
:
operation failed in interpreter:

        def batch_norm(input : Tensor, running_mean : Optional[Tensor], running_var : Optional[Tensor], training : bool, momentum : float, eps : float) -> Tensor:
            if training:
                norm_mean, norm_var = torch.batch_norm_update_stats(input, running_mean, running_var, momentum)
                                      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ <--- HERE
            else:
                norm_mean = torch._unwrap_optional(running_mean)
                norm_var = torch._unwrap_optional(running_var)
            norm_mean = torch._ncf_unsqueeze(norm_mean, input.dim())
            norm_var = torch._ncf_unsqueeze(norm_var, input.dim())
            norm_invstd = 1 / (eps + torch.sqrt(norm_var))
            return ((input - norm_mean) * norm_invstd)