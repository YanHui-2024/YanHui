WARNING: ThreadSanitizer: data race (pid=3634939)
  Write of size 8 at 0x7b1c001a8398 by thread T104 (mutexes: write M150199):
    #0 torch::jit::ProfilingRecord::instrumentGraph(std::shared_ptr<torch::jit::Graph> const&)::$_1::operator()(std::vector<c10::IValue, std::allocator<c10::IValue> >&) const caffe2/torch/csrc/jit/runtime/profiling_record.cpp:320 (libcaffe2_libtorch.so+0x35c0d08)
    #1 std::_Function_handler<void (std::vector<c10::IValue, std::allocator<c10::IValue> >&), torch::jit::ProfilingRecord::instrumentGraph(std::shared_ptr<torch::jit::Graph> const&)::$_1>::_M_invoke(std::_Any_data const&, std::vector<c10::IValue, std::allocator<c10::IValue> >&) 
    #2 std::function<void (std::vector<c10::IValue, std::allocator<c10::IValue> >&)>::operator()(std::vector<c10::IValue, std::allocator<c10::IValue> >&) const 
    #3 torch::jit::InterpreterStateImpl::runImpl(std::vector<c10::IValue, std::allocator<c10::IValue> >&) caffe2/torch/csrc/jit/runtime/interpreter.cpp:440 (libcaffe2_libtorch.so+0x30efc55)
    #4 torch::jit::InterpreterStateImpl::runAsync(std::vector<c10::IValue, std::allocator<c10::IValue> >&) caffe2/torch/csrc/jit/runtime/interpreter.cpp:723 (libcaffe2_libtorch.so+0x30d1c9a)
    #5 torch::jit::InterpreterState::runAsync(std::vector<c10::IValue, std::allocator<c10::IValue> >&) caffe2/torch/csrc/jit/runtime/interpreter.cpp:844 (libcaffe2_libtorch.so+0x30d1bf7)
    #6 torch::jit::GraphExecutorImplBase::runAsync(std::vector<c10::IValue, std::allocator<c10::IValue> >&, std::function<void (std::function<void ()>)>) caffe2/torch/csrc/jit/runtime/graph_executor.cpp:571 (libcaffe2_libtorch.so+0x2ef4d4b)
    #7 torch::jit::GraphExecutor::runAsync(std::vector<c10::IValue, std::allocator<c10::IValue> >&, std::function<void (std::function<void ()>)>) caffe2/torch/csrc/jit/runtime/graph_executor.cpp:772 (libcaffe2_libtorch.so+0x2ef5951)
    #8 torch::jit::GraphFunction::runAsync(std::vector<c10::IValue, std::allocator<c10::IValue> >&, std::function<void (std::function<void ()>)>) caffe2/torch/csrc/jit/api/function_impl.cpp:45 (libcaffe2_libtorch.so+0x2ed78f3)

  Previous read of size 8 at 0x7b1c001a8398 by thread T102 (mutexes: write M150190):
    #0 torch::jit::ProfilingRecord::ready() const caffe2/torch/csrc/jit/runtime/profiling_record.h:201 (libcaffe2_libtorch.so+0x35a4d99)
    #1 torch::jit::ProfilingGraphExecutorImpl::getOptimizedPlanFor(std::vector<c10::IValue, std::allocator<c10::IValue> >&, unsigned long) caffe2/torch/csrc/jit/runtime/profiling_graph_executor_impl.cpp:613 (libcaffe2_libtorch.so+0x35a4239)
    #2 torch::jit::ProfilingGraphExecutorImpl::getPlanFor(std::vector<c10::IValue, std::allocator<c10::IValue> >&, unsigned long) caffe2/torch/csrc/jit/runtime/profiling_graph_executor_impl.cpp:640 (libcaffe2_libtorch.so+0x35a4ea9)
    #3 torch::jit::GraphExecutor::getPlanFor(std::vector<c10::IValue, std::allocator<c10::IValue> >&, unsigned long) caffe2/torch/csrc/jit/runtime/graph_executor.cpp:782 (libcaffe2_libtorch.so+0x2ef5a13)
    #4 torch::jit::InterpreterStateImpl::runGraphFunction(std::vector<c10::IValue, std::allocator<c10::IValue> >&, torch::jit::Function*) caffe2/torch/csrc/jit/runtime/interpreter.cpp:202 (libcaffe2_libtorch.so+0x30f31cf)
    #5 torch::jit::InterpreterStateImpl::runImpl(std::vector<c10::IValue, std::allocator<c10::IValue> >&) caffe2/torch/csrc/jit/runtime/interpreter.cpp:330 (libcaffe2_libtorch.so+0x30eee38)
    #6 torch::jit::InterpreterStateImpl::runAsync(std::vector<c10::IValue, std::allocator<c10::IValue> >&) caffe2/torch/csrc/jit/runtime/interpreter.cpp:723 (libcaffe2_libtorch.so+0x30d1c9a)
    #7 torch::jit::InterpreterState::runAsync(std::vector<c10::IValue, std::allocator<c10::IValue> >&) caffe2/torch/csrc/jit/runtime/interpreter.cpp:844 (libcaffe2_libtorch.so+0x30d1bf7)
    #8 torch::jit::GraphExecutorImplBase::runAsync(std::vector<c10::IValue, std::allocator<c10::IValue> >&, std::function<void (std::function<void ()>)>) caffe2/torch/csrc/jit/runtime/graph_executor.cpp:571 (libcaffe2_libtorch.so+0x2ef4d4b)
    #9 torch::jit::GraphExecutor::runAsync(std::vector<c10::IValue, std::allocator<c10::IValue> >&, std::function<void (std::function<void ()>)>) caffe2/torch/csrc/jit/runtime/graph_executor.cpp:772 (libcaffe2_libtorch.so+0x2ef5951)
    #10 torch::jit::GraphFunction::runAsync(std::vector<c10::IValue, std::allocator<c10::IValue> >&, std::function<void (std::function<void ()>)>) caffe2/torch/csrc/jit/api/function_impl.cpp:45 (libcaffe2_libtorch.so+0x2ed78f3)