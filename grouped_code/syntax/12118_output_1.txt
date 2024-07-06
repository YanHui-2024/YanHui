#0  0x000055555563fe37 in PyErr_Fetch ()
#1  0x00007fffe603a9e3 in pybind11::error_scope::error_scope (this=0x7fffffffc130) at /root/pytorch/third_party/pybind11/include/pybind11/detail/common.h:715
#2  pybind11::error_already_set::~error_already_set (this=0x5555b1c9f4f0, __in_chrg=<optimized out>)
    at /root/pytorch/third_party/pybind11/include/pybind11/pybind11.h:1890
#3  0x00007fffcf58bc8a in __gxx_exception_cleanup (code=<optimized out>, exc=0x5555b1c9f4d0)
    at /opt/conda/conda-bld/compilers_linux-64_1534514838838/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libstdc++-v3/libsupc++/eh_throw.cc:49
#4  0x00007fffd480c719 in torch::jit::InterpreterStateImpl::runOneStage(std::vector<torch::jit::IValue, std::allocator<torch::jit::IValue> >&) ()
   from /root/miniconda3/lib/python3.5/site-packages/torch/lib/libtorch.so.1
#5  0x00007fffd47eb524 in torch::jit::GraphExecutorImpl::run(std::vector<torch::jit::IValue, std::allocator<torch::jit::IValue> >&) ()
   from /root/miniconda3/lib/python3.5/site-packages/torch/lib/libtorch.so.1
#6  0x00007fffe62e73e0 in torch::jit::script::Method::run (stack=..., this=0x5555b1213450) at /root/pytorch/torch/csrc/jit/script/module.h:60
#7  torch::jit::invokeScriptMethodFromPython (method=..., args=..., kwargs=...) at /root/pytorch/torch/csrc/jit/pybind_utils.h:299
#8  0x00007fffe62ca7ed in torch::jit::script::<lambda(torch::jit::script::Module&, pybind11::args, pybind11::kwargs)>::operator() (__closure=<optimized out>, 
    kwargs=..., args=..., self=...) at torch/csrc/jit/script/init.cpp:498