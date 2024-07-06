frame #11: 0x0000000112e71ab9 _C.cpython-37m-darwin.so`torch::jit::script::pythonResolver(this=0x0000000101aecf40, name="torch", m=0x000000011c8a52f0, loc=0x00007ffeefbf6360)>)::$_0::operator()(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, torch::jit::script::Method&, torch::jit::SourceRange const&) const at init.cpp:367
   364 	             Method& m,
   365 	             const SourceRange& loc) -> std::shared_ptr<SugaredValue> {
   366 	    AutoGIL ag;
-> 367 	    py::object obj = rcb(name);
   368 	    if (obj.is(py::none())) {
   369 	      return nullptr;
   370 	    }
(lldb) p rcb
(torch::jit::script::ResolutionCallback) $0 = 0x0000000101aca650
(lldb) p name
(std::__1::string) $1 = "torch"