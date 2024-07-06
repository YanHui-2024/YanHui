graph(%0 : Float(5, 3, 10)
      %1 : Long(3)
      %2 : Float(2, 3, 20)
      %3 : Float(20, 10)
      %4 : Float(20, 20)
      %5 : Float(20)
      %6 : Float(20)
      %7 : Float(20, 20)
      %8 : Float(20, 20)
      %9 : Float(20)
      %10 : Float(20)) {
  %11 : bool = prim::Constant[value=0](), scope: RNNTest
  %12 : Long(3) = aten::_cast_Long(%1, %11), scope: RNNTest
  %13 : bool = prim::Constant[value=0](), scope: RNNTest
  %14 : Float(12, 10), %15 : Long(5) = aten::_pack_padded_sequence(%0, %12, %13), scope: RNNTest
  %16 : int = prim::Constant[value=0](), scope: RNNTest/RNN[rnn]
  %17 : int = prim::Constant[value=0](), scope: RNNTest/RNN[rnn]
  %18 : Long() = aten::select(%15, %16, %17), scope: RNNTest/RNN[rnn]
  %19 : int = prim::Constant[value=-1](), scope: RNNTest/RNN[rnn]
  %20 : int = aten::size(%14, %19), scope: RNNTest/RNN[rnn]
  %21 : Long() = prim::NumToTensor(%20), scope: RNNTest/RNN[rnn]
  %22 : int = prim::Constant[value=10](), scope: RNNTest/RNN[rnn]
  %23 : Byte() = aten::ne(%21, %22), scope: RNNTest/RNN[rnn]
  %24 : int = prim::Constant[value=0](), scope: RNNTest/RNN[rnn]
  %25 : int = prim::Constant[value=0](), scope: RNNTest/RNN[rnn]
  %26 : Long() = aten::select(%15, %24, %25), scope: RNNTest/RNN[rnn]
  %27 : int = prim::Constant[value=0](), scope: RNNTest/RNN[rnn]
  %28 : int = aten::size(%2, %27), scope: RNNTest/RNN[rnn]
  %29 : Long() = prim::NumToTensor(%28), scope: RNNTest/RNN[rnn]
  %30 : int = prim::Constant[value=1](), scope: RNNTest/RNN[rnn]
  %31 : int = aten::size(%2, %30), scope: RNNTest/RNN[rnn]
  %32 : Long() = prim::NumToTensor(%31), scope: RNNTest/RNN[rnn]
  %33 : int = prim::Constant[value=2](), scope: RNNTest/RNN[rnn]
  %34 : int = aten::size(%2, %33), scope: RNNTest/RNN[rnn]
  %35 : Long() = prim::NumToTensor(%34), scope: RNNTest/RNN[rnn]
  %36 : int = prim::Constant[value=2](), scope: RNNTest/RNN[rnn]
  %37 : Byte() = aten::eq(%29, %36), scope: RNNTest/RNN[rnn]
  %38 : int = prim::Constant[value=3](), scope: RNNTest/RNN[rnn]
  %39 : Byte() = aten::eq(%32, %38), scope: RNNTest/RNN[rnn]
  %40 : int = prim::Constant[value=20](), scope: RNNTest/RNN[rnn]
  %41 : Byte() = aten::eq(%35, %40), scope: RNNTest/RNN[rnn]
  %42 : Dynamic[] = prim::ListConstruct(%3, %4, %5, %6, %7, %8, %9, %10), scope: RNNTest/RNN[rnn]
  %43 : bool = prim::Constant[value=1](), scope: RNNTest/RNN[rnn]
  %44 : int = prim::Constant[value=2](), scope: RNNTest/RNN[rnn]
  %45 : float = prim::Constant[value=0](), scope: RNNTest/RNN[rnn]
  %46 : bool = prim::Constant[value=1](), scope: RNNTest/RNN[rnn]
  %47 : bool = prim::Constant[value=0](), scope: RNNTest/RNN[rnn]
  %48 : Float(12, 20), %49 : Float(2, 3, 20) = aten::rnn_tanh(%14, %15, %2, %42, %43, %44, %45, %46, %47), scope: RNNTest/RNN[rnn]
  %50 : int = prim::Constant[value=0](), scope: RNNTest
  %51 : int = aten::size(%15, %50), scope: RNNTest
  %52 : Long() = prim::NumToTensor(%51), scope: RNNTest
  %53 : bool = prim::Constant[value=0](), scope: RNNTest
  %54 : float = prim::Constant[value=0](), scope: RNNTest
  %55 : int = prim::Constant[value=5](), scope: RNNTest
  %56 : Float(5, 3, 20), %57 : Long(3) = aten::_pad_packed_sequence(%48, %15, %53, %54, %55), scope: RNNTest
  return ();
}

graph(%0 : Float(5, 3, 10)
      %1 : Long(3)
      %2 : Float(2, 3, 20)
      %3 : Float(20, 10)
      %4 : Float(20, 20)
      %5 : Float(20)
      %6 : Float(20)
      %7 : Float(20, 20)
      %8 : Float(20, 20)
      %9 : Float(20)
      %10 : Float(20)) {
  %11 : bool = prim::Constant[value=0](), scope: RNNTest
  %12 : Long(3) = aten::_cast_Long(%1, %11), scope: RNNTest
  %13 : bool = prim::Constant[value=0](), scope: RNNTest
  %14 : Float(12, 10), %15 : Long(5) = aten::_pack_padded_sequence(%0, %12, %13), scope: RNNTest
  %16 : int = prim::Constant[value=0](), scope: RNNTest/RNN[rnn]
  %17 : int = prim::Constant[value=0](), scope: RNNTest/RNN[rnn]
  %18 : Long() = aten::select(%15, %16, %17), scope: RNNTest/RNN[rnn]
  %19 : int = prim::Constant[value=-1](), scope: RNNTest/RNN[rnn]
  %20 : int = aten::size(%14, %19), scope: RNNTest/RNN[rnn]
  %21 : Long() = prim::NumToTensor(%20), scope: RNNTest/RNN[rnn]
  %22 : int = prim::Constant[value=10](), scope: RNNTest/RNN[rnn]
  %23 : Byte() = aten::ne(%21, %22), scope: RNNTest/RNN[rnn]
  %24 : int = prim::Constant[value=0](), scope: RNNTest/RNN[rnn]
  %25 : int = prim::Constant[value=0](), scope: RNNTest/RNN[rnn]
  %26 : Long() = aten::select(%15, %24, %25), scope: RNNTest/RNN[rnn]
  %27 : int = prim::Constant[value=0](), scope: RNNTest/RNN[rnn]
  %28 : int = aten::size(%2, %27), scope: RNNTest/RNN[rnn]
  %29 : Long() = prim::NumToTensor(%28), scope: RNNTest/RNN[rnn]
  %30 : int = prim::Constant[value=1](), scope: RNNTest/RNN[rnn]
  %31 : int = aten::size(%2, %30), scope: RNNTest/RNN[rnn]
  %32 : Long() = prim::NumToTensor(%31), scope: RNNTest/RNN[rnn]
  %33 : int = prim::Constant[value=2](), scope: RNNTest/RNN[rnn]
  %34 : int = aten::size(%2, %33), scope: RNNTest/RNN[rnn]
  %35 : Long() = prim::NumToTensor(%34), scope: RNNTest/RNN[rnn]
  %36 : int = prim::Constant[value=2](), scope: RNNTest/RNN[rnn]
  %37 : Byte() = aten::eq(%29, %36), scope: RNNTest/RNN[rnn]
  %38 : int = prim::Constant[value=3](), scope: RNNTest/RNN[rnn]
  %39 : Byte() = aten::eq(%32, %38), scope: RNNTest/RNN[rnn]
  %40 : int = prim::Constant[value=20](), scope: RNNTest/RNN[rnn]
  %41 : Byte() = aten::eq(%35, %40), scope: RNNTest/RNN[rnn]
  %42 : Dynamic[] = prim::ListConstruct(%3, %4, %5, %6, %7, %8, %9, %10), scope: RNNTest/RNN[rnn]
  %43 : bool = prim::Constant[value=1](), scope: RNNTest/RNN[rnn]
  %44 : int = prim::Constant[value=2](), scope: RNNTest/RNN[rnn]
  %45 : float = prim::Constant[value=0](), scope: RNNTest/RNN[rnn]
  %46 : bool = prim::Constant[value=1](), scope: RNNTest/RNN[rnn]
  %47 : bool = prim::Constant[value=0](), scope: RNNTest/RNN[rnn]
  %48 : Float(12, 20), %49 : Float(2, 3, 20) = aten::rnn_tanh(%14, %15, %2, %42, %43, %44, %45, %46, %47), scope: RNNTest/RNN[rnn]
  %50 : int = prim::Constant[value=0](), scope: RNNTest
  %51 : int = aten::size(%15, %50), scope: RNNTest
  %52 : Long() = prim::NumToTensor(%51), scope: RNNTest
  %53 : bool = prim::Constant[value=0](), scope: RNNTest
  %54 : float = prim::Constant[value=0](), scope: RNNTest
  %55 : int = prim::Constant[value=5](), scope: RNNTest
  %56 : Float(5, 3, 20), %57 : Long(3) = aten::_pad_packed_sequence(%48, %15, %53, %54, %55), scope: RNNTest
  return ();
}

None
Traceback (most recent call last):
  File "rnn_test.py", line 25, in <module>
    traced(x, lengths, h0)
  File "/Users/jamesreed/onnx-fairseq/pytorch/torch/nn/modules/module.py", line 477, in __call__
    result = self.forward(*input, **kwargs)
  File "/Users/jamesreed/onnx-fairseq/pytorch/torch/jit/__init__.py", line 1179, in forward
    return self._get_method('forward')(*args, **kwargs)
RuntimeError: 
Expected total_length to be at least the length of the longest sequence in input, but got total_length=5 and max sequence length being 7 (_pad_packed_sequence at ../aten/src/ATen/native/PackedSequence.cpp:115)
frame #0: at::TypeDefault::_pad_packed_sequence(at::Tensor const&, at::Tensor const&, bool, at::Scalar, long long) const + 167 (0x118ae9397 in libcaffe2.dylib)
frame #1: torch::autograd::VariableType::_pad_packed_sequence(at::Tensor const&, at::Tensor const&, bool, at::Scalar, long long) const + 1836 (0x11c148c6c in libtorch.dylib)
frame #2: at::_pad_packed_sequence(at::Tensor const&, at::Tensor const&, bool, at::Scalar, long long) + 194 (0x11c4ea5b2 in libtorch.dylib)
frame #3: torch::jit::(anonymous namespace)::$_25::operator()(std::__1::vector<c10::IValue, std::__1::allocator<c10::IValue> >&) const + 431 (0x11c4ea41f in libtorch.dylib)
frame #4: int std::__1::__invoke_void_return_wrapper<int>::__call<torch::jit::(anonymous namespace)::$_25&, std::__1::vector<c10::IValue, std::__1::allocator<c10::IValue> >&>(torch::jit::(anonymous namespace)::$_25&&&, std::__1::vector<c10::IValue, std::__1::allocator<c10::IValue> >&&&) + 77 (0x11c4ea25d in libtorch.dylib)
frame #5: std::__1::__function::__func<torch::jit::(anonymous namespace)::$_25, std::__1::allocator<torch::jit::(anonymous namespace)::$_25>, int (std::__1::vector<c10::IValue, std::__1::allocator<c10::IValue> >&)>::operator()(std::__1::vector<c10::IValue, std::__1::allocator<c10::IValue> >&) + 68 (0x11c4ea154 in libtorch.dylib)
frame #6: std::__1::function<int (std::__1::vector<c10::IValue, std::__1::allocator<c10::IValue> >&)>::operator()(std::__1::vector<c10::IValue, std::__1::allocator<c10::IValue> >&) const + 121 (0x1175e6b39 in _C.cpython-36m-darwin.so)
frame #7: torch::jit::InterpreterStateImpl::run(std::__1::vector<c10::IValue, std::__1::allocator<c10::IValue> >&) + 304 (0x11c9436c0 in libtorch.dylib)
frame #8: torch::jit::InterpreterState::run(std::__1::vector<c10::IValue, std::__1::allocator<c10::IValue> >&) + 40 (0x11c943588 in libtorch.dylib)
frame #9: torch::jit::(anonymous namespace)::ExecutionPlan::run(std::__1::vector<c10::IValue, std::__1::allocator<c10::IValue> >&) const + 46 (0x11c8c9f2e in libtorch.dylib)
frame #10: torch::jit::GraphExecutorImpl::run(std::__1::vector<c10::IValue, std::__1::allocator<c10::IValue> >&) + 544 (0x11c8c0b60 in libtorch.dylib)
frame #11: torch::jit::GraphExecutor::run(std::__1::vector<c10::IValue, std::__1::allocator<c10::IValue> >&) + 40 (0x11c8c0938 in libtorch.dylib)
frame #12: torch::jit::script::Method::run(std::__1::vector<c10::IValue, std::__1::allocator<c10::IValue> >&) + 1144 (0x117769838 in _C.cpython-36m-darwin.so)
frame #13: torch::jit::invokeScriptMethodFromPython(torch::jit::script::Method&, torch::jit::tuple_slice, pybind11::kwargs) + 207 (0x1177692ef in _C.cpython-36m-darwin.so)
frame #14: torch::jit::script::initJitScriptBindings(_object*)::$_19::operator()(pybind11::args, pybind11::kwargs) const + 321 (0x11776ad91 in _C.cpython-36m-darwin.so)
frame #15: pybind11::object pybind11::detail::argument_loader<pybind11::args, pybind11::kwargs>::call_impl<pybind11::object, torch::jit::script::initJitScriptBindings(_object*)::$_19&, 0ul, 1ul, pybind11::detail::void_type>(torch::jit::script::initJitScriptBindings(_object*)::$_19&&&, pybind11::detail::index_sequence<0ul, 1ul>, pybind11::detail::void_type&&) + 216 (0x11776abe8 in _C.cpython-36m-darwin.so)
frame #16: std::__1::enable_if<!(std::is_void<pybind11::object>::value), pybind11::object>::type pybind11::detail::argument_loader<pybind11::args, pybind11::kwargs>::call<pybind11::object, pybind11::detail::void_type, torch::jit::script::initJitScriptBindings(_object*)::$_19&>(torch::jit::script::initJitScriptBindings(_object*)::$_19&&&) + 56 (0x11776aaf8 in _C.cpython-36m-darwin.so)
frame #17: void pybind11::cpp_function::initialize<torch::jit::script::initJitScriptBindings(_object*)::$_19, pybind11::object, pybind11::args, pybind11::kwargs, pybind11::name, pybind11::is_method, pybind11::sibling>(torch::jit::script::initJitScriptBindings(_object*)::$_19&&, pybind11::object (*)(pybind11::args, pybind11::kwargs), pybind11::name const&, pybind11::is_method const&, pybind11::sibling const&)::'lambda'(pybind11::detail::function_call&)::operator()(pybind11::detail::function_call&) const + 223 (0x11776aa0f in _C.cpython-36m-darwin.so)
frame #18: void pybind11::cpp_function::initialize<torch::jit::script::initJitScriptBindings(_object*)::$_19, pybind11::object, pybind11::args, pybind11::kwargs, pybind11::name, pybind11::is_method, pybind11::sibling>(torch::jit::script::initJitScriptBindings(_object*)::$_19&&, pybind11::object (*)(pybind11::args, pybind11::kwargs), pybind11::name const&, pybind11::is_method const&, pybind11::sibling const&)::'lambda'(pybind11::detail::function_call&)::__invoke(pybind11::detail::function_call&) + 24 (0x11776a918 in _C.cpython-36m-darwin.so)
frame #19: pybind11::cpp_function::dispatcher(_object*, _object*, _object*) + 6919 (0x116fa2dd7 in _C.cpython-36m-darwin.so)
<omitting python frames>
frame #48: start + 1 (0x7fff78774015 in libdyld.dylib)
:
operation failed in interpreter:
/Users/jamesreed/onnx-fairseq/pytorch/torch/nn/utils/rnn.py(193): pad_packed_sequence
rnn_test.py(13): forward
/Users/jamesreed/onnx-fairseq/pytorch/torch/nn/modules/module.py(465): _slow_forward
/Users/jamesreed/onnx-fairseq/pytorch/torch/nn/modules/module.py(475): __call__
/Users/jamesreed/onnx-fairseq/pytorch/torch/jit/__init__.py(572): trace
rnn_test.py(19): <module>