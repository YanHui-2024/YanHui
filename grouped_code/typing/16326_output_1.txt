unknown file: Failure
C++ exception with description "Type cannot be accurately recovered from this IValue. (incompleteInferTypeFrom at aten/src/ATen/core/type.cpp:149)
frame #0: c10::Error::Error(c10::SourceLocation, std::string const&) + 0x45 (0x7fccd18b6dd5 in /home/sidney/bazel/av/bin/tests/../../lib/third_party/libc10.so)
frame #1: c10::incompleteInferTypeFrom(c10::IValue const&) + 0x3b4 (0x7fccbc189ac4 in /home/sidney/bazel/av/bin/tests/../../lib/third_party/libcaffe2.so)
frame #2: torch::jit::script::Method::checkInputsAgainstSchema(std::vector<c10::IValue, std::allocator<c10::IValue> >&) + 0xa8 (0x40f448 in ./bin/tests/intentnet_test)
