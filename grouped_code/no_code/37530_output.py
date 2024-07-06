Program received signal SIGSEGV, Segmentation fault.         
0x00007fffbb68d0de in ?? () from /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
(gdb) bt                                                                                          
#0  0x00007fffbb68d0de in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#1  0x00007fffbb67c882 in c10::Type::isSubtypeOfExt(std::shared_ptr<c10::Type>, std::ostream*) const () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#2  0x00007fffbb67c967 in c10::ListType::isSubtypeOfExt(std::shared_ptr<c10::Type>, std::ostream*) const () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#3  0x00007fffbb68af88 in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#4  0x00007fffbdb3a2b4 in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#5  0x00007fffbdb60d52 in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#6  0x00007fffbdb6277f in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#7  0x00007fffbdb6414c in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#8  0x00007fffbdb233eb in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#9  0x00007fffbdbf3f4c in torch::jit::GraphFunction::ensure_defined() () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#10 0x00007fffbdb223f1 in torch::jit::CompilationUnit::define(c10::optional<c10::QualifiedName> const&, std::vector<torch::jit::Def, std::allocator<torch::jit::Def> > const&, std::vector<std::shar
ed_ptr<torch::jit::Resolver>, std::allocator<std::shared_ptr<torch::jit::Resolver> > > const&, torch::jit::Self const*, bool) () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#11 0x00007fffc0b093bb in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_python.so
#12 0x00007fffc0b0981c in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_python.so
#13 0x00007fffc0800576 in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_python.so
#14 0x00007ffff7b28ff6 in PyCFunction_Call () at /usr/lib/libpython3.8.so.1.0
#15 0x00007ffff7b1c3d2 in _PyObject_MakeTpCall () at /usr/lib/libpython3.8.so.1.0
#16 0x00007ffff7bd979c in _PyEval_EvalFrameDefault () at /usr/lib/libpython3.8.so.1.0
#17 0x00007ffff7bc6a9d in _PyFunction_Vectorcall () at /usr/lib/libpython3.8.so.1.0
#18 0x00007ffff7b223fd in PyObject_Call () at /usr/lib/libpython3.8.so.1.0
#19 0x00007fffc0b5f91d in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_python.so
#20 0x00007fffc0af5bdc in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_python.so
#21 0x00007fffbdb400b6 in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#22 0x00007fffbdb3af72 in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#23 0x00007fffbdb437c1 in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#24 0x00007fffbdb431d7 in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#25 0x00007fffbdb436f5 in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#26 0x00007fffbdb5441d in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#27 0x00007fffbdb555eb in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#28 0x00007fffbdb5c97a in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#29 0x00007fffbdb627d1 in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#30 0x00007fffbdb6414c in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#31 0x00007fffbdb233eb in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#32 0x00007fffbdbf3f4c in torch::jit::GraphFunction::ensure_defined() () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#33 0x00007fffbdb223f1 in torch::jit::CompilationUnit::define(c10::optional<c10::QualifiedName> const&, std::vector<torch::jit::Def, std::allocator<torch::jit::Def> > const&, std::vector<std::shar
ed_ptr<torch::jit::Resolver>, std::allocator<std::shared_ptr<torch::jit::Resolver> > > const&, torch::jit::Self const*, bool) () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#34 0x00007fffc0b0c783 in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_python.so
#35 0x00007fffc0800576 in  () at /usr/lib/python3.8/site-packages/torch/lib/libtorch_python.so