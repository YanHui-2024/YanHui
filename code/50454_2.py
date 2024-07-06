hread 1 "python3" received signal SIGSEGV, Segmentation fault.
0x00007fffd610d8db in pybind11::detail::type_caster_base<torch::jit::Node>::cast(torch::jit::Node const*, pybind11::return_value_policy, pybind11::handle) ()
   from /private/home/xxx/pytorch/torch/lib/libtorch_python.so
(gdb) bt
#0  0x00007fffd610d8db in pybind11::detail::type_caster_base<torch::jit::Node>::cast(torch::jit::Node const*, pybind11::return_value_policy, pybind11::handle) ()
   from /private/home/xxx/pytorch/torch/lib/libtorch_python.so
#1  0x00007fffd6110fb4 in pybind11::cpp_function::initialize<pybind11::make_iterator<(pybind11::return_value_policy)6, torch::jit::generic_graph_node_list_iterator<torch::jit::Node>, torch::jit::generic_graph_node_list_iterator<torch::jit::Node>, torch::jit::Node*>(torch::jit::generic_graph_node_list_iterator<torch::jit::Node>, torch::jit::generic_graph_node_list_iterator<torch::jit::Node>)::{lambda(pybind11::detail::iterator_state<torch::jit::generic_graph_node_list_iterator<torch::jit::Node>, torch::jit::generic_graph_node_list_iterator<torch::jit::Node>, false, (pybind11::return_value_policy)6>&)#2}, torch::jit::Node*, pybind11::detail::iterator_state<torch::jit::generic_graph_node_list_iterator<torch::jit::Node>, torch::jit::generic_graph_node_list_iterator<torch::jit::Node>, false, (pybind11::return_value_policy)6>&, pybind11::name, pybind11::is_method, pybind11::sibling, pybind11::return_value_policy>(pybind11::make_iterator<(pybind11::return_value_policy)6, torch::jit::generic_graph_node_list_iterator<torch::jit::Node>, torch::jit::generic_graph_node_list_iterator<torch::jit::Node>, torch::jit::Node*>(torch::jit::generic_graph_node_list_iterator<torch::jit::Node>, torch::jit::generic_graph_node_list_iterator<torch::jit::Node>)::{lambda(pybind11::detail::iterator_state<torch::jit::generic_graph_node_list_iterator<torch::jit::Node>, torch::jit::generic_graph_node_list_iterator<torch::jit::Node>, false, (pybind11::return_value_policy)6>&)#2}&&, torch::jit::Node* (*)(pybind11::detail::iterator_state<torch::jit::generic_graph_node_list_iterator<torch::jit::Node>, torch::jit::generic_graph_node_list_iterator<torch::jit::Node>, false, (pybind11::return_value_policy)6>&), pybind11::name const&, pybind11::is_method const&, pybind11::sibling const&, pybind11::return_value_policy const&)::{lambda(pybind11::detail::function_call&)#3}::_FUN(pybind11::detail::function_call) () from /private/home/xxx/pytorch/torch/lib/libtorch_python.so
#2  0x00007fffd5de165f in pybind11::cpp_function::dispatcher(_object*, _object*, _object*) () from /private/home/xxx/pytorch/torch/lib/libtorch_python.so
#3  0x00005555556c9c96 in cfunction_call_varargs (kwargs=<optimized out>,
    args=<optimized out>, func=0x7ffeeceb12c0)
    at /tmp/build/80754af9/python_1573076469108/work/Objects/call.c:742
#4  PyCFunction_Call (func=0x7ffeeceb12c0, args=<optimized out>, kwargs=<optimized out>)
    at /tmp/build/80754af9/python_1573076469108/work/Objects/call.c:772
#5  0x000055555568631f in _PyObject_MakeTpCall (callable=0x7ffeeceb12c0,
    args=<optimized out>, nargs=<optimized out>, keywords=<optimized out>)
    at /tmp/build/80754af9/python_1573076469108/work/Objects/call.c:159
#6  0x00005555556d628f in _PyObject_Vectorcall (kwnames=0x0, nargsf=1,
    args=0x7fffffffb988, callable=0x7ffeeceb12c0)
    at /tmp/build/80754af9/python_1573076469108/work/Include/cpython/abstract.h:125
#7  method_vectorcall (method=<optimized out>, args=0x0, nargsf=<optimized out>,
    kwnames=<optimized out>)
    at /tmp/build/80754af9/python_1573076469108/work/Objects/classobject.c:67
#8  0x00005555555cf098 in _PyObject_Vectorcall (callable=0x7ffeed5452c0,
--Type <RET> for more, q to quit, c to continue without paging--
    ut>, nargsf=<optimized out>, kwnames=<optimized out>) at /tmp/build/80754af9/python_1573076469108/work/Include/cpython/abstract.h:127
#9  0x00005555556c8a21 in _PyObject_FastCall () at /tmp/build/80754af9/python_1573076469108/work/Include/cpython/abstract.h:147
#10 call_unbound (nargs=<optimized out>, args=<optimized out>, self=<optimized out>, func=<optimized out>, unbound=<optimized out>) at /tmp/build/80754af9/python_1573076469108/work/Objects/typeobject.c:1451
#11 call_method (nargs=0, args=0x0, name=0x5555558a6c20 <PyId___next__.15142>, obj=0x7fff90405af0) at /tmp/build/80754af9/python_1573076469108/work/Objects/typeobject.c:1480
#12 slot_tp_iternext (self=0x7fff90405af0) at /tmp/build/80754af9/python_1573076469108/work/Objects/typeobject.c:6695
#13 0x00005555556ccbb4 in list_extend (iterable=<optimized out>, self=0x7ffeed8c7a40) at /tmp/build/80754af9/python_1573076469108/work/Objects/listobject.c:953
#14 list___init___impl (iterable=<optimized out>, self=0x7ffeed8c7a40) at /tmp/build/80754af9/python_1573076469108/work/Objects/listobject.c:2723
#15 list___init__ (self=0x7ffeed8c7a40, args=<optimized out>, kwargs=<optimized out>) at /tmp/build/80754af9/python_1573076469108/work/Objects/clinic/listobject.c.h:329
#16 0x0000555555686294 in type_call (kwds=0x0, args=0x7ffff781ad60, type=<optimized out>) at /tmp/build/80754af9/python_1573076469108/work/Objects/typeobject.c:989
#17 _PyObject_MakeTpCall (callable=0x5555558c3240 <PyList_Type>, args=<optimized out>, nargs=<optimized out>, keywords=<optimized out>) at /tmp/build/80754af9/python_1573076469108/work/Objects/call.c:159
#18 0x000055555570d945 in _PyObject_Vectorcall (kwnames=0x0, nargsf=<optimized out>, args=0x7ffff78437b8, callable=<optimized out>) at /tmp/build/80754af9/python_1573076469108/work/Include/cpython/abstract.h:125
#19 call_function (kwnames=0x0, oparg=<optimized out>, pp_stack=<synthetic pointer>, tstate=0x5555558e9590) at /tmp/build/80754af9/python_1573076469108/work/Python/ceval.c:4987
#20 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1573076469108/work/Python/ceval.c:3500
#21 0x00005555556d4c32 in _PyEval_EvalCodeWithName (_co=0x7ffff77f9d40, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=0x0, kwargs=0x0, kwcount=<optimized out>, kwstep=2, defs=0x0, defcount=0,
    kwdefs=0x0, closure=0x0, name=0x0, qualname=0x0) at /tmp/build/80754af9/python_1573076469108/work/Python/ceval.c:4298
#22 0x00005555556d5a04 in PyEval_EvalCodeEx (_co=<optimized out>, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kws=<optimized out>, kwcount=0, defs=0x0, defcount=0, kwdefs=0x0, closure=0x0)
    at /tmp/build/80754af9/python_1573076469108/work/Python/ceval.c:4327
#23 0x0000555555768f5c in PyEval_EvalCode (co=<optimized out>, globals=<optimized out>, locals=<optimized out>) at /tmp/build/80754af9/python_1573076469108/work/Python/ceval.c:718
#24 0x0000555555769004 in run_eval_code_obj (co=0x7ffff77f9d40, globals=0x7ffff78ae540, locals=0x7ffff78ae540) at /tmp/build/80754af9/python_1573076469108/work/Python/pythonrun.c:1117
#25 0x000055555579e304 in run_mod (mod=<optimized out>, filename=<optimized out>, globals=0x7ffff78ae540, locals=0x7ffff78ae540, flags=<optimized out>, arena=<optimized out>) at /tmp/build/80754af9/python_1573076469108/work/Python/pythonrun.c:1139
#26 0x00005555557a0c50 in PyRun_FileExFlags (fp=<optimized out>, filename_str=<optimized out>, start=<optimized out>, globals=0x7ffff78ae540, locals=0x7ffff78ae540, closeit=1, flags=0x7fffffffbe68)
    at /tmp/build/80754af9/python_1573076469108/work/Python/pythonrun.c:1055
#27 0x00005555557a0e41 in PyRun_SimpleFileExFlags (fp=0x5555558e7d10, filename=<optimized out>, closeit=1, flags=0x7fffffffbe68) at /tmp/build/80754af9/python_1573076469108/work/Python/pythonrun.c:428
#28 0x00005555557a1983 in pymain_run_file (cf=0x7fffffffbe68, config=0x5555558e86a0) at /tmp/build/80754af9/python_1573076469108/work/Modules/main.c:381
#29 pymain_run_python (exitcode=0x7fffffffbe60) at /tmp/build/80754af9/python_1573076469108/work/Modules/main.c:565
#30 Py_RunMain () at /tmp/build/80754af9/python_1573076469108/work/Modules/main.c:644
#31 0x00005555557a1bc9 in Py_BytesMain (argc=<optimized out>, argv=<optimized out>) at /tmp/build/80754af9/python_1573076469108/work/Modules/main.c:698
#32 0x00007ffff7db50b3 in __libc_start_main (main=0x55555565e720 <main>, argc=2, argv=0x7fffffffc068, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffc058) at ../csu/libc-start.c:308
#33 0x000055555572ae13 in _start () at ../sysdeps/x86_64/elf/start.S:103
