> AddressSanitizer:DEADLYSIGNAL
> =================================================================
> ==920756==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000018 (pc 0x7f8b08065f17 bp 0x7ffec7afec30 sp 0x7ffec7afec10 T0)
> === How to use this, how to get the raw stack trace, and more: fburl.com/ASAN ===
> ==920756==The signal is caused by a READ memory access.
> ==920756==Hint: address points to the zero page.
> SCARINESS: 10 (null-deref)
>      #0 caffe2/aten/src/ATen/core/jit_type.h:137 c10::Type::kind() const
>      #1 caffe2/aten/src/ATen/core/jit_type.h:153 std::shared_ptr<...> c10::Type::cast<...>()
>      #2 caffe2/aten/src/ATen/core/jit_type.h:282 c10::OptionalType::create(std::shared_ptr<...>)
>     #3 0x7f8b08cb7d59 in torch::jit::initPythonIRBindings(_object*)::$_89::operator()(std::shared_ptr<...>) const caffe2/torch/csrc/jit/python/python_ir.cpp:761:23:14:14:19:14:19:14:19:14:14:19:14:14:19:14:16
>     #164 python3.7+0x400689                       _start
> 
> AddressSanitizer can not provide additional info.
> SUMMARY: AddressSanitizer: SEGV caffe2/aten/src/ATen/core/jit_type.h:137 in c10::Type::kind() const
> ==920756==ABORTING