  "AsanReport": [
    "==142006== ERROR: libFuzzer: deadly signal\n",
    "[Detaching after fork from child process 142353]\n",
    "    #0 0x59ec11 in __sanitizer_print_stack_trace /llvm-project/compiler-rt/lib/asan/asan_stack.cpp:87:3\n",
    "    #1 0x513547 in fuzzer::PrintStackTrace() /llvm-project/compiler-rt/lib/fuzzer/FuzzerUtil.cpp:210:5\n",
    "    #2 0x4f9753 in fuzzer::Fuzzer::CrashCallback() /llvm-project/compiler-rt/lib/fuzzer/FuzzerLoop.cpp:233:3\n",
    "    #3 0x7f402f8a63bf  (/lib/x86_64-linux-gnu/libpthread.so.0+0x153bf)\n",
    "    #4 0x7f402f6c818a in __libc_signal_restore_set /build/glibc-eX1tMB/glibc-2.31/signal/../sysdeps/unix/sysv/linux/internal-signals.h:86:3\n",
    "    #5 0x7f402f6c818a in raise /build/glibc-eX1tMB/glibc-2.31/signal/../sysdeps/unix/sysv/linux/raise.c:48:3\n",
    "    #6 0x7f402f6a7858 in abort /build/glibc-eX1tMB/glibc-2.31/stdlib/abort.c:79:7\n",
    "    #7 0x7f402fab2910  (/lib/x86_64-linux-gnu/libstdc++.so.6+0x9e910)\n",
    "    #8 0x7f402fabe38b  (/lib/x86_64-linux-gnu/libstdc++.so.6+0xaa38b)\n",
    "    #9 0x7f402fabe3f6 in std::terminate() (/lib/x86_64-linux-gnu/libstdc++.so.6+0xaa3f6)\n",
    "    #10 0x7f402fabe6a8 in __cxa_throw (/lib/x86_64-linux-gnu/libstdc++.so.6+0xaa6a8)\n",
    "    #11 0x7f402fab53aa  (/lib/x86_64-linux-gnu/libstdc++.so.6+0xa13aa)\n",
    "    #12 0x6a4cdf in std::vector<c10::IValue, std::allocator<c10::IValue> >::_M_range_check(unsigned long) const /usr/bin/../lib/gcc/x86_64-linux-gnu/10/../../../../include/c++/10/bits/stl_vector.h:1073:4\n",
    "    #13 0x9315ee3 in std::vector<c10::IValue, std::allocator<c10::IValue> >::at(unsigned long) const /usr/bin/../lib/gcc/x86_64-linux-gnu/10/../../../../include/c++/10/bits/stl_vector.h:1112:2\n",
    "    #14 0x9315ee3 in c10::ivalue::TupleElements::at(unsigned long) const /pytorch_fuzz/aten/src/ATen/core/ivalue_inl.h:501:30\n",
    "    #15 0x9ec5505 in torch::jit::restoreAccurateTypeTags(c10::IValue const&, c10::Type::SingletonOrSharedTypePtr<c10::Type> const&) /pytorch_fuzz/torch/csrc/jit/serialization/unpickler.cpp:97:64\n",
    "    #16 0x9e0514b in torch::jit::(anonymous namespace)::ScriptModuleDeserializer::readArchive(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)::$_1::operator()(c10::StrongTypePtr const&, c10::IValue) const /pytorch_fuzz/torch/csrc/jit/serialization/import.cpp:157:7\n",
    "    #17 0x9e0514b in c10::intrusive_ptr<c10::ivalue::Object, c10::detail::intrusive_target_default_null_type<c10::ivalue::Object> > std::__invoke_impl<c10::intrusive_ptr<c10::ivalue::Object, c10::detail::intrusive_target_default_null_type<c10::ivalue::Object> >, torch::jit::(anonymous namespace)::ScriptModuleDeserializer::readArchive(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)::$_1&, c10::StrongTypePtr, c10::IValue>(std::__invoke_other, torch::jit::(anonymous namespace)::ScriptModuleDeserializer::readArchive(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)::$_1&, c10::StrongTypePtr&&, c10::IValue&&) /usr/bin/../lib/gcc/x86_64-linux-gnu/10/../../../../include/c++/10/bits/invoke.h:60:14\n",
    "    #18 0x9e044b0 in std::enable_if<__and_<std::__not_<std::is_void<c10::intrusive_ptr<c10::ivalue::Object, c10::detail::intrusive_target_default_null_type<c10::ivalue::Object> > > >, std::is_convertible<std::__invoke_result<torch::jit::(anonymous namespace)::ScriptModuleDeserializer::readArchive(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)::$_1&, c10::StrongTypePtr, c10::IValue>::type, c10::intrusive_ptr<c10::ivalue::Object, c10::detail::intrusive_target_default_null_type<c10::ivalue::Object> > > >::value, c10::intrusive_ptr<c10::ivalue::Object, c10::detail::intrusive_target_default_null_type<c10::ivalue::Object> > >::type std::__invoke_r<c10::intrusive_ptr<c10::ivalue::Object, c10::detail::intrusive_target_default_null_type<c10::ivalue::Object> >, torch::jit::(anonymous namespace)::ScriptModuleDeserializer::readArchive(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)::$_1&, c10::StrongTypePtr, c10::IValue>(torch::jit::(anonymous namespace)::ScriptModuleDeserializer::readArchive(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)::$_1&, c10::StrongTypePtr&&, c10::IValue&&) /usr/bin/../lib/gcc/x86_64-linux-gnu/10/../../../../include/c++/10/bits/invoke.h:141:14\n",
    "    #19 0x9e0431b in std::_Function_handler<c10::intrusive_ptr<c10::ivalue::Object, c10::detail::intrusive_target_default_null_type<c10::ivalue::Object> > (c10::StrongTypePtr, c10::IValue), torch::jit::(anonymous namespace)::ScriptModuleDeserializer::readArchive(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)::$_1>::_M_invoke(std::_Any_data const&, c10::StrongTypePtr&&, c10::IValue&&) /usr/bin/../lib/gcc/x86_64-linux-gnu/10/../../../../include/c++/10/bits/std_function.h:291:9\n",
    "    #20 0x9eed44d in std::function<c10::intrusive_ptr<c10::ivalue::Object, c10::detail::intrusive_target_default_null_type<c10::ivalue::Object> > (c10::StrongTypePtr, c10::IValue)>::operator()(c10::StrongTypePtr, c10::IValue) const /usr/bin/../lib/gcc/x86_64-linux-gnu/10/../../../../include/c++/10/bits/std_function.h:622:14\n",
    "    #21 0x9eed0ee in torch::jit::Unpickler::readGlobal(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)::$_9::operator()() const /pytorch_fuzz/torch/csrc/jit/serialization/unpickler.cpp:704:20\n",
    "    #22 0x9eed0ee in void std::__invoke_impl<void, torch::jit::Unpickler::readGlobal(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)::$_9&>(std::__invoke_other, torch::jit::Unpickler::readGlobal(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)::$_9&) /usr/bin/../lib/gcc/x86_64-linux-gnu/10/../../../../include/c++/10/bits/invoke.h:60:14\n",
    "    #23 0x9ecb6d4 in torch::jit::Unpickler::readInstruction() /pytorch_fuzz/torch/csrc/jit/serialization/unpickler.cpp:444:7\n",
    "    #24 0x9ec9ac7 in torch::jit::Unpickler::run() /pytorch_fuzz/torch/csrc/jit/serialization/unpickler.cpp:226:27\n",
    "    #25 0x9ec9762 in torch::jit::Unpickler::parse_ivalue() /pytorch_fuzz/torch/csrc/jit/serialization/unpickler.cpp:183:3\n",
    "    #26 0x9e0c84e in torch::jit::readArchiveAndTensors(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, c10::optional<std::function<c10::StrongTypePtr (c10::QualifiedName const&)> >, c10::optional<std::function<c10::intrusive_ptr<c10::ivalue::Object, c10::detail::intrusive_target_default_null_type<c10::ivalue::Object> > (c10::StrongTypePtr, c10::IValue)> >, c10::optional<c10::Device>, caffe2::serialize::PyTorchStreamReader&, c10::Type::SingletonOrSharedTypePtr<c10::Type> (*)(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&), std::shared_ptr<torch::jit::DeserializationStorageContext>) /pytorch_fuzz/torch/csrc/jit/serialization/import_read.cpp:54:20\n",
    "    #27 0x9e02779 in torch::jit::(anonymous namespace)::ScriptModuleDeserializer::readArchive(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) /pytorch_fuzz/torch/csrc/jit/serialization/import.cpp:171:10\n",
    "    #28 0x9dfe60b in torch::jit::(anonymous namespace)::ScriptModuleDeserializer::deserialize(c10::optional<c10::Device>, std::unordered_map<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::hash<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::equal_to<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >&) /pytorch_fuzz/torch/csrc/jit/serialization/import.cpp:274:19\n",
    "    #29 0x9e013c4 in torch::jit::load(std::shared_ptr<caffe2::serialize::ReadAdapterInterface>, c10::optional<c10::Device>, std::unordered_map<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::hash<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::equal_to<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >&) /pytorch_fuzz/torch/csrc/jit/serialization/import.cpp:403:23\n",
    "    #30 0x9e01977 in torch::jit::load(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, c10::optional<c10::Device>, std::unordered_map<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::hash<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::equal_to<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >&) /pytorch_fuzz/torch/csrc/jit/serialization/import.cpp:375:17\n",
    "    #31 0x9e0176c in torch::jit::load(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, c10::optional<c10::Device>) /pytorch_fuzz/torch/csrc/jit/serialization/import.cpp:367:10\n",
    "    #32 0x5cdfd2 in LLVMFuzzerTestOneInput /load_fuzz.cc:45:18\n",
    "    #33 0x4fac81 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) /llvm-project/compiler-rt/lib/fuzzer/FuzzerLoop.cpp:611:15\n",
    "    #34 0x4e4b9c in fuzzer::RunOneTest(fuzzer::Fuzzer*, char const*, unsigned long) /llvm-project/compiler-rt/lib/fuzzer/FuzzerDriver.cpp:324:6\n",
    "    #35 0x4ea8eb in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) /llvm-project/compiler-rt/lib/fuzzer/FuzzerDriver.cpp:860:9\n",
    "    #36 0x513e82 in main /llvm-project/compiler-rt/lib/fuzzer/FuzzerMain.cpp:20:10\n",
    "    #37 0x7f402f6a90b2 in __libc_start_main /build/glibc-eX1tMB/glibc-2.31/csu/../csu/libc-start.c:308:16\n",
    "    #38 0x4df4bd in _start (/fuzz/load_fuzz+0x4df4bd)\n",