offset < args.size() ASSERT FAILED at /Users/soumith/mc3build/conda-bld/pytorch_1549593514549/work/torch/csrc/jit/argument_spec.h:99, please report a bug to PyTorch. (addInput at /Users/soumith/mc3build/conda-bld/pytorch_1549593514549/work/torch/csrc/jit/argument_spec.h:99)
frame #0: c10::Error::Error(c10::SourceLocation, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&) + 64 (0x10d3ddff0 in libc10.dylib)
frame #1: torch::jit::ArgumentSpec::addInput(c10::IValue const&, unsigned long&, bool) + 1100 (0x115e1df9c in libtorch.1.dylib)
frame #2: torch::jit::ArgumentSpec::addInput(c10::IValue const&, unsigned long&, bool) + 401 (0x115e1dce1 in libtorch.1.dylib)
frame #3: torch::jit::ArgumentSpec::ArgumentSpec(bool, c10::ArrayRef<c10::IValue>, unsigned long) + 145 (0x115e1da01 in libtorch.1.dylib)
frame #4: torch::jit::GraphExecutorImpl::run(std::__1::vector<c10::IValue, std::__1::allocator<c10::IValue> >&) + 184 (0x115e145d8 in libtorch.1.dylib)
frame #5: torch::jit::script::Method::run(std::__1::vector<c10::IValue, std::__1::allocator<c10::IValue> >&) + 216 (0x109a6d908 in libtorch_python.dylib)
frame #6: torch::jit::invokeScriptMethodFromPython(torch::jit::script::Method&, torch::jit::tuple_slice, pybind11::kwargs) + 163 (0x109a6d773 in libtorch_python.dylib)
frame #7: void pybind11::cpp_function::initialize<torch::jit::script::initJitScriptBindings(_object*)::$_17, pybind11::object, pybind11::args, pybind11::kwargs, pybind11::name, pybind11::is_method, pybind11::sibling>(torch::jit::script::initJitScriptBindings(_object*)::$_17&&, pybind11::object (*)(pybind11::args, pybind11::kwargs), pybind11::name const&, pybind11::is_method const&, pybind11::sibling const&)::'lambda'(pybind11::detail::function_call&)::__invoke(pybind11::detail::function_call&) + 342 (0x109a6d3f6 in libtorch_python.dylib)
frame #8: pybind11::cpp_function::dispatcher(_object*, _object*, _object*) + 3482 (0x1096b55fa in libtorch_python.dylib)
<omitting python frames>