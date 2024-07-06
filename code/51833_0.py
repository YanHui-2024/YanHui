#0  0x0000555558c8d470 in ?? ()
#1  0x00007ffd87360315 in c10::operator<< (out=..., t=...) at ../aten/src/ATen/core/type.cpp:120
#2  0x00007ffd8b443c8f in torch::jit::operator<< (out=..., l=...) at ../torch/csrc/jit/ir/ir.cpp:98
#3  0x00007ffd8b44551b in torch::jit::Graph::print (this=0x555558c8de60, out=..., print_source_locations=true)
    at ../torch/csrc/jit/ir/ir.cpp:320
#4  0x00007ffd8b453468 in torch::jit::Graph::toString[abi:cxx11](bool) const (this=0x555558c8de60, 
    print_source_locations=true) at ../torch/csrc/jit/ir/ir.cpp:1841
#5  0x00007ffd97a8b7a9 in torch::jit::<lambda(torch::jit::Graph&)>::operator()(torch::jit::Graph &) const (
    __closure=0x5555582ce288, g=...) at ../torch/csrc/jit/python/python_ir.cpp:215
#6  0x00007ffd97aba3c7 in pybind11::detail::argument_loader<torch::jit::Graph&>::call_impl<std::__cxx11::basic_string<char>, torch::jit::initPythonIRBindings(PyObject*)::<lambda(torch::jit::Graph&)>&, 0, pybind11::detail::void_type>(torch::jit::<lambda(torch::jit::Graph&)> &, std::index_sequence, pybind11::detail::void_type &&) (this=0x7fffffff7cb0, f=...)
    at ../torch/include/pybind11/cast.h:2042
#7  0x00007ffd97ab60cf in pybind11::detail::argument_loader<torch::jit::Graph&>::call<std::__cxx11::basic_string<char>, pybind11::detail::void_type, torch::jit::initPythonIRBindings(PyObject*)::<lambda(torch::jit::Graph&)>&>(torch::jit::<lambda(torch::jit::Graph&)> &) (this=0x7fffffff7cb0, f=...) at ../torch/include/pybind11/cast.h:2014
#8  0x00007ffd97aa3c17 in pybind11::cpp_function::<lambda(pybind11::detail::function_call&)>::operator()(pybind11::detail::function_call &) const (this=0x0, call=...) at ../torch/include/pybind11/pybind11.h:192
#9  0x00007ffd97aa3cbd in pybind11::cpp_function::<lambda(pybind11::detail::function_call&)>::_FUN(pybind11::detail::function_call &) () at ../torch/include/pybind11/pybind11.h:170
#10 0x00007ffd9732da78 in pybind11::cpp_function::dispatcher (self=0x7ffd507a34b0, args_in=0x7ffd44844bb0, kwargs_in=0x0)
    at ../torch/include/pybind11/pybind11.h:767