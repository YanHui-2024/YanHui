    [1/3] Building CXX object caffe2/CMakeFiles/torch_cuda.dir/__/torch/csrc/jit/codegen/cuda/type.cpp.o
    FAILED: caffe2/CMakeFiles/torch_cuda.dir/__/torch/csrc/jit/codegen/cuda/type.cpp.o
    /home/cloudhan/ccache/lib/c++  -DAT_PARALLEL_OPENMP=1 -DHAVE_MALLOC_USABLE_SIZE=1 -DHAVE_MMAP=1 -DHAVE_SHM_OPEN=1 -DHAVE_SHM_UNLINK=1 -DMINIZ_DISABLE_ZIP_READER_CRC32_CHECKS -DONNXIFI_ENABLE_EXT=1 -DONNX_ML=1 -DONNX_NAMESPACE=onnx_torch -DTORCH_CUDA_BUILD_MAIN_LIB -DUSE_NCCL -D_FILE_OFFSET_BITS=64 -Dtorch_cuda_EXPORTS -Iaten/src -I../aten/src -I. -I../ -I../third_party/onnx -Ithird_party/onnx -I../third_party/foxi -Ithird_party/foxi -Icaffe2/aten/src/TH -I../aten/src/TH -Icaffe2/aten/src/THC -I../aten/src/THC -I../aten/src/THCUNN -I../aten/src/ATen/cuda -Icaffe2/aten/src -I../aten/../third_party/catch/single_include -I../aten/src/ATen/.. -Icaffe2/aten/src/ATen -Inccl/include -I../c10/cuda/../.. -I../c10/.. -I../caffe2/../torch/csrc/api -I../caffe2/../torch/csrc/api/include -isystem ../third_party/protobuf/src -isystem ../third_party/XNNPACK/include -isystem ../cmake/../third_party/eigen -isystem /home/cloudhan/miniconda3/include/python3.7m -isystem /home/cloudhan/miniconda3/lib/python3.7/site-packages/numpy/core/include -isystem ../cmake/../third_party/pybind11/include -isystem ../cmake/../third_party/cub -isystem /usr/local/cuda-10.0/include -fvisibility-inlines-hidden -fopenmp -DUSE_XNNPACK -DUSE_INTERNAL_THREADPOOL_IMPL -O2 -fPIC -Wno-narrowing -Wall -Wextra -Werror=return-type -Wno-missing-field-initializers -Wno-type-limits -Wno-array-bounds -Wno-unknown-pragmas -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -Wno-unused-result -Wno-strict-overflow -Wno-strict-aliasing -Wno-error=deprecated-declarations -Wno-error=pedantic -Wno-error=redundant-decls -Wno-error=old-style-cast -fdiagnostics-color=always -Wno-unused-but-set-variable -Wno-maybe-uninitialized -fno-math-errno -fno-trapping-math -Werror=format -DHAVE_AVX_CPU_DEFINITION -DHAVE_AVX2_CPU_DEFINITION -O2 -g -DNDEBUG -fPIC   -DCUDA_HAS_FP16=1 -DHAVE_GCC_GET_CPUID -DUSE_AVX -DUSE_AVX2 -DTH_HAVE_THREAD -Wall -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -Wno-write-strings -Wno-unknown-pragmas -Wno-missing-braces -Wno-maybe-uninitialized -fvisibility=hidden -O2 -DTORCH_CUDA_BUILD_MAIN_LIB -fopenmp -pthread -std=gnu++14 -MD -MT caffe2/CMakeFiles/torch_cuda.dir/__/torch/csrc/jit/codegen/cuda/type.cpp.o -MF caffe2/CMakeFiles/torch_cuda.dir/__/torch/csrc/jit/codegen/cuda/type.cpp.o.d -o caffe2/CMakeFiles/torch_cuda.dir/__/torch/csrc/jit/codegen/cuda/type.cpp.o -c ../torch/csrc/jit/codegen/cuda/type.cpp
    In file included from /usr/include/c++/5/bits/hashtable.h:35:0,
                     from /usr/include/c++/5/unordered_map:47,
                     from ../c10/util/typeid.h:11,
                     from ../c10/core/ScalarType.h:8,
                     from ../torch/csrc/jit/codegen/cuda/type.h:3,
                     from ../torch/csrc/jit/codegen/cuda/type.cpp:1:
    /usr/include/c++/5/bits/hashtable_policy.h: In instantiation of ‘struct std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> >’:
    /usr/include/c++/5/type_traits:137:12:   required from ‘struct std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > >’
    /usr/include/c++/5/type_traits:148:38:   required from ‘struct std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
    /usr/include/c++/5/bits/unordered_set.h:95:63:   required from ‘class std::unordered_set<torch::jit::fuser::BinaryOpType>’
    ../torch/csrc/jit/codegen/cuda/type.cpp:185:41:   required from here
    /usr/include/c++/5/bits/hashtable_policy.h:85:34: error: no match for call to ‘(const std::hash<torch::jit::fuser::BinaryOpType>) (const torch::jit::fuser::BinaryOpType&)’
      noexcept(declval<const _Hash&>()(declval<const _Key&>()))>
                                      ^
    In file included from /usr/include/c++/5/bits/move.h:57:0,
                     from /usr/include/c++/5/bits/stl_pair.h:59,
                     from /usr/include/c++/5/bits/stl_algobase.h:64,
                     from /usr/include/c++/5/bits/char_traits.h:39,
                     from /usr/include/c++/5/ios:40,
                     from /usr/include/c++/5/istream:38,
                     from /usr/include/c++/5/sstream:38,
                     from ../c10/macros/Macros.h:150,
                     from ../c10/util/SmallVector.h:24,
                     from ../c10/util/ArrayRef.h:18,
                     from ../c10/core/ScalarType.h:3,
                     from ../torch/csrc/jit/codegen/cuda/type.h:3,
                     from ../torch/csrc/jit/codegen/cuda/type.cpp:1:
    /usr/include/c++/5/type_traits: In instantiation of ‘struct std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’:
    /usr/include/c++/5/bits/unordered_set.h:95:63:   required from ‘class std::unordered_set<torch::jit::fuser::BinaryOpType>’
    ../torch/csrc/jit/codegen/cuda/type.cpp:185:41:   required from here
    /usr/include/c++/5/type_traits:148:38: error: ‘value’ is not a member of ‘std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > >’
         : public integral_constant<bool, !_Pp::value>
                                          ^
    In file included from /usr/include/c++/5/unordered_set:48:0,
                     from ../c10/util/typeid.h:12,
                     from ../c10/core/ScalarType.h:8,
                     from ../torch/csrc/jit/codegen/cuda/type.h:3,
                     from ../torch/csrc/jit/codegen/cuda/type.cpp:1:
    /usr/include/c++/5/bits/unordered_set.h: In instantiation of ‘class std::unordered_set<torch::jit::fuser::BinaryOpType>’:
    ../torch/csrc/jit/codegen/cuda/type.cpp:185:41:   required from here
    /usr/include/c++/5/bits/unordered_set.h:95:63: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           typedef __uset_hashtable<_Value, _Hash, _Pred, _Alloc>  _Hashtable;
                                                                   ^
    /usr/include/c++/5/bits/unordered_set.h:102:45: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           typedef typename _Hashtable::key_type key_type;
                                                 ^
    /usr/include/c++/5/bits/unordered_set.h:103:47: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           typedef typename _Hashtable::value_type value_type;
                                                   ^
    /usr/include/c++/5/bits/unordered_set.h:104:43: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           typedef typename _Hashtable::hasher hasher;
                                               ^
    /usr/include/c++/5/bits/unordered_set.h:105:46: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           typedef typename _Hashtable::key_equal key_equal;
                                                  ^
    /usr/include/c++/5/bits/unordered_set.h:106:51: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           typedef typename _Hashtable::allocator_type allocator_type;
                                                       ^
    /usr/include/c++/5/bits/unordered_set.h:111:45: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           typedef typename _Hashtable::pointer  pointer;
                                                 ^
    /usr/include/c++/5/bits/unordered_set.h:112:50: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           typedef typename _Hashtable::const_pointer const_pointer;
                                                      ^
    /usr/include/c++/5/bits/unordered_set.h:113:47: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           typedef typename _Hashtable::reference  reference;
                                                   ^
    /usr/include/c++/5/bits/unordered_set.h:114:52: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           typedef typename _Hashtable::const_reference const_reference;
                                                        ^
    /usr/include/c++/5/bits/unordered_set.h:115:46: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           typedef typename _Hashtable::iterator  iterator;
                                                  ^
    /usr/include/c++/5/bits/unordered_set.h:116:51: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           typedef typename _Hashtable::const_iterator const_iterator;
                                                       ^
    /usr/include/c++/5/bits/unordered_set.h:117:51: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           typedef typename _Hashtable::local_iterator local_iterator;
                                                       ^
    /usr/include/c++/5/bits/unordered_set.h:118:57: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           typedef typename _Hashtable::const_local_iterator const_local_iterator;
                                                             ^
    /usr/include/c++/5/bits/unordered_set.h:119:47: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           typedef typename _Hashtable::size_type  size_type;
                                                   ^
    /usr/include/c++/5/bits/unordered_set.h:120:52: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           typedef typename _Hashtable::difference_type difference_type;
                                                        ^
    /usr/include/c++/5/bits/unordered_set.h:274:7: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           operator=(initializer_list<value_type> __l)
           ^
    /usr/include/c++/5/bits/unordered_set.h:368:2: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
      emplace(_Args&&... __args)
      ^
    /usr/include/c++/5/bits/unordered_set.h:412:7: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           insert(const value_type& __x)
           ^
    /usr/include/c++/5/bits/unordered_set.h:416:7: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           insert(value_type&& __x)
           ^
    /usr/include/c++/5/bits/unordered_set.h:471:7: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           insert(initializer_list<value_type> __l)
           ^
    /usr/include/c++/5/bits/unordered_set.h:616:7: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           equal_range(const key_type& __x)
           ^
    /usr/include/c++/5/bits/unordered_set.h:620:7: error: ‘value’ is not a member of ‘std::__not_<std::__and_<std::__is_fast_hash<std::hash<torch::jit::fuser::BinaryOpType> >, std::__detail::__is_noexcept_hash<torch::jit::fuser::BinaryOpType, std::hash<torch::jit::fuser::BinaryOpType> > > >’
           equal_range(const key_type& __x) const
           ^
    ../torch/csrc/jit/codegen/cuda/type.cpp:191:76: error: too many initializers for ‘std::unordered_set<torch::jit::fuser::BinaryOpType>’
                                                                BinaryOpType::NE};
                                                                                ^
    ../torch/csrc/jit/codegen/cuda/type.cpp: In function ‘bool torch::jit::fuser::is_logical_op(const torch::jit::fuser::BinaryOpType&)’:
    ../torch/csrc/jit/codegen/cuda/type.cpp:194:29: error: ‘class std::unordered_set<torch::jit::fuser::BinaryOpType>’ has no member named ‘count’
       return logical_binary_ops.count(bot) > 0;
                                 ^
