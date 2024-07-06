Traceback (most recent call last):
  File "/usr/local/lib/python3.7/dist-packages/torch/jit/__init__.py", line 529, in run_mod_and_filter_tensor_outputs
    outs = wrap_retval(mod(*_clone_inputs(inputs)))
  File "/usr/local/lib/python3.7/dist-packages/torch/nn/modules/module.py", line 493, in __call__
    result = self.forward(*input, **kwargs)
  File "/usr/local/lib/python3.7/dist-packages/torch/jit/__init__.py", line 1407, in forward
    return self._get_method('forward')(*args, **kwargs)
RuntimeError: elementMap_.count(v) ASSERT FAILED at /pytorch/torch/csrc/jit/passes/alias_analysis.cpp:536, please report a bug to PyTorch. (registerWrite at /pytorch/torch/csrc/jit/passes/alias_analysis.cpp:536)
frame #0: std::function<std::string ()>::operator()() const + 0x11 (0x7fce0a6322a1 in /usr/local/lib/python3.7/dist-packages/torch/lib/libc10.so)
frame #1: c10::Error::Error(c10::SourceLocation, std::string const&) + 0x2a (0x7fce0a631bda in /usr/local/lib/python3.7/dist-packages/torch/lib/libc10.so)
frame #2: torch::jit::AliasDb::registerWrite(torch::jit::Value const*, torch::jit::Node*) + 0x1dd (0x7fce035b48bd in /usr/local/lib/python3.7/dist-packages/torch/lib/libtorch.so.1)
frame #3: torch::jit::AliasDb::analyzeImpl(torch::jit::Node*) + 0x675 (0x7fce035b5aa5 in /usr/local/lib/python3.7/dist-packages/torch/lib/libtorch.so.1)
frame #4: torch::jit::AliasDb::analyze(torch::jit::Node*) + 0xf (0x7fce035b64bf in /usr/local/lib/python3.7/dist-packages/torch/lib/libtorch.so.1)
frame #5: torch::jit::AliasDb::analyze(torch::jit::Block*) + 0x33 (0x7fce035b65a3 in /usr/local/lib/python3.7/dist-packages/torch/lib/libtorch.so.1)
frame #6: torch::jit::AliasDb::analyze(std::shared_ptr<torch::jit::Graph> const&) + 0x92c (0x7fce035b84cc in /usr/local/lib/python3.7/dist-packages/torch/lib/libtorch.so.1)
frame #7: torch::jit::AliasDb::AliasDb(std::shared_ptr<torch::jit::Graph>) + 0x3a8 (0x7fce035b8d98 in /usr/local/lib/python3.7/dist-packages/torch/lib/libtorch.so.1)
frame #8: torch::unique_type_for<torch::jit::AliasDb>::value torch::make_unique<torch::jit::AliasDb, std::shared_ptr<torch::jit::Graph>&>(std::shared_ptr<torch::jit::Graph>&) + 0x45 (0x7fce035d89e5 in /usr/local/lib/python3.7/dist-packages/torch/lib/libtorch.so.1)
frame #9: <unknown function> + 0xace7f5 (0x7fce035ce7f5 in /usr/local/lib/python3.7/dist-packages/torch/lib/libtorch.so.1)
frame #10: <unknown function> + 0xad5758 (0x7fce035d5758 in /usr/local/lib/python3.7/dist-packages/torch/lib/libtorch.so.1)
frame #11: <unknown function> + 0xad71d7 (0x7fce035d71d7 in /usr/local/lib/python3.7/dist-packages/torch/lib/libtorch.so.1)
frame #12: torch::jit::FuseGraph(std::shared_ptr<torch::jit::Graph>&) + 0x65 (0x7fce035d82e5 in /usr/local/lib/python3.7/dist-packages/torch/lib/libtorch.so.1)
frame #13: <unknown function> + 0xa64cd6 (0x7fce03564cd6 in /usr/local/lib/python3.7/dist-packages/torch/lib/libtorch.so.1)
frame #14: <unknown function> + 0x479015 (0x7fce0ad07015 in /usr/local/lib/python3.7/dist-packages/torch/lib/libtorch_python.so)
frame #15: <unknown function> + 0x450c0a (0x7fce0acdec0a in /usr/local/lib/python3.7/dist-packages/torch/lib/libtorch_python.so)
frame #16: <unknown function> + 0x1302fc (0x7fce0a9be2fc in /usr/local/lib/python3.7/dist-packages/torch/lib/libtorch_python.so)
<omitting python frames>
frame #18: python3() [0x4d9dc7]
frame #20: python3() [0x58f132]
frame #25: python3() [0x4d9e62]
frame #30: python3() [0x58f08b]
frame #44: python3() [0x54af20]
frame #50: python3() [0x630f22]
frame #53: python3() [0x65414e]
frame #55: __libc_start_main + 0xeb (0x7fce0ea74b6b in /lib/x86_64-linux-gnu/libc.so.6)