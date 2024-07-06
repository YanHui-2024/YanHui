---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-3-334d309cf512> in <module>
----> 1 lltm_cpp = load(name="lltm_cpp", sources=["lltm.cpp"])

/usr/lib/python3.10/site-packages/torch/utils/cpp_extension.py in load(name, sources, extra_cflags, extra_cuda_cflags, extra_ldflags, extra_include_paths, build_directory, verbose, with_cuda, is_python_module, is_standalone, keep_intermediates)
   1122                 verbose=True)
   1123     '''
-> 1124     return _jit_compile(
   1125         name,
   1126         [sources] if isinstance(sources, str) else sources,

/usr/lib/python3.10/site-packages/torch/utils/cpp_extension.py in _jit_compile(name, sources, extra_cflags, extra_cuda_cflags, extra_ldflags, extra_include_paths, build_directory, verbose, with_cuda, is_python_module, is_standalone, keep_intermediates)
   1360         return _get_exec_path(name, build_directory)
   1361 
-> 1362     return _import_module_from_library(name, build_directory, is_python_module)
   1363 
   1364 

/usr/lib/python3.10/site-packages/torch/utils/cpp_extension.py in _import_module_from_library(module_name, path, is_python_module)
   1751         spec = importlib.util.spec_from_file_location(module_name, filepath)
   1752         module = importlib.util.module_from_spec(spec)
-> 1753         assert isinstance(spec.loader, importlib.abc.Loader)
   1754         spec.loader.exec_module(module)
   1755         return module

AttributeError: module 'importlib' has no attribute 'abc'
