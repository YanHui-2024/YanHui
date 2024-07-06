Terminate c10::Error(Type cannot be accurately recovered from this IValue. (incompleteInferTypeFrom at ../aten/src/ATen/core/type.cpp:149) frame #0: c10::Error::Error(c10::SourceLocation, std::string const&) + 0x45 ( in ../lib/third_party/libc10.so) frame #1: c10::incompleteInferTypeFrom(c10::IValue const&) + 0x3b4 ( in ../lib/third_party/libcaffe2.so) frame #2: c10::isSubvalueOf(c10::IValue const&, std::shared_ptr<c10::Type>) + 0x25 ( in ../lib/third_party/libcaffe2.so) frame #3: <unknown function> + 0x5b54d0 ( in ../lib/third_party/libcaffe2.so) frame #4: c10::isSubvalueOf(c10::IValue const&, std::shared_ptr<c10::Type>) + 0x15e ( in ../lib/third_party/libcaffe2.so) frame #5: torch::jit::script::Method::checkInputsAgainstSchema(std::vector<c10::IValue, std::allocator<c10::IValue> >&) + 0x268 ( in ../lib/libml_libtorch_estimator.so) frame #6: torch::jit::script::Module::forward(std::vector<c10::IValue, std::allocator<c10::IValue> >) + 0x71 ( in ../lib/libml_libtorch_estimator.so) frame #7: std::map<std::string, at::Tensor, std::less<std::string>, std::allocator<std::pair<std::string const, at::Tensor> > > ml::libtorch_estimator::infer<at::Tensor>(bool) + 0x228 ( in ../lib/libml_libtorch_estimator.so) frame #8: load_and_run_model(std::string) + 0x1643 ( in ./bin/inference) frame #9: main + 0x154 ( in ./bin/inference) frame #10: __libc_start_main + 0xf5 ( in /lib/x86_64-linux-gnu/libc.so.6) frame #11: ./bin/inference() [] ) {
  libstdc++.so.6.0.19 5e6d6 eh_terminate.cc:42 __cxxabiv1::__terminate(void (*)())
  libstdc++.so.6.0.19 5e703
  libstdc++.so.6.0.19 5e922
  libcaffe2.so 5b4dbb c10::incompleteInferTypeFrom(c10::IValue const&)
  libcaffe2.so 5b5275 c10::isSubvalueOf(c10::IValue const&, std::shared_ptr<c10::Type>)
  libcaffe2.so 5b54d0 c10::isSubvalueOf(c10::IValue const&, std::shared_ptr<c10::Type>)::{lambda(c10::IValue const&)#1}::operator()(c10::IValue const&) const
  libcaffe2.so 5b53ae c10::isSubvalueOf(c10::IValue const&, std::shared_ptr<c10::Type>)
  libml_libtorch_estimator.so 1c448 torch::jit::script::Method::checkInputsAgainstSchema(std::vector<c10::IValue, std::allocator<c10::IValue> >&)
  libml_libtorch_estimator.so 141d1 torch::jit::script::Module::forward(std::vector<c10::IValue, std::allocator<c10::IValue> >)
  libml_libtorch_estimator.so 10b48 std::map<std::string, at::Tensor, std::less<std::string>, std::allocator<std::pair<std::string const, at::Tensor> > > ml::libtorch_estimator::infer<at::Tensor>(bool)
  inference 40c483 load_and_run_model(std::string)
  inference 40e184 main
  libc-2.19.so 21f45 libc-start.c:321 __libc_start_main
  inference 40ad77 _start
}
terminate called after throwing an instance of 'c10::Error'
  what():  Type cannot be accurately recovered from this IValue. (incompleteInferTypeFrom at ../aten/src/ATen/core/type.cpp:149)
frame #0: c10::Error::Error(c10::SourceLocation, std::string const&) + 0x45 ( in ../lib/third_party/libc10.so)
frame #1: c10::incompleteInferTypeFrom(c10::IValue const&) + 0x3b4 ( in ../lib/third_party/libcaffe2.so)
frame #2: c10::isSubvalueOf(c10::IValue const&, std::shared_ptr<c10::Type>) + 0x25 ( in ../lib/third_party/libcaffe2.so)
frame #3: <unknown function> + 0x5b54d0 ( in ../lib/third_party/libcaffe2.so)
frame #4: c10::isSubvalueOf(c10::IValue const&, std::shared_ptr<c10::Type>) + 0x15e ( in ../lib/third_party/libcaffe2.so)
frame #5: torch::jit::script::Method::checkInputsAgainstSchema(std::vector<c10::IValue, std::allocator<c10::IValue> >&) + 0x268 ( in ../lib/libml_libtorch_estimator.so)
frame #6: torch::jit::script::Module::forward(std::vector<c10::IValue, std::allocator<c10::IValue> >) + 0x71 ( in ../lib/libml_libtorch_estimator.so)
frame #7: std::map<std::string, at::Tensor, std::less<std::string>, std::allocator<std::pair<std::string const, at::Tensor> > > ml::libtorch_estimator::infer<at::Tensor>(bool) + 0x228 ( in ../lib/libml_libtorch_estimator.so)
frame #8: load_and_run_model(std::string) + 0x1643 ( in ./bin/inference)
frame #9: main + 0x154 ( in ./bin/inference)
frame #10: __libc_start_main + 0xf5 ( in /lib/x86_64-linux-gnu/libc.so.6)
frame #11: ./bin/inference() []