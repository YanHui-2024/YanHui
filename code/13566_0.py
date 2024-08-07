import os
import torch
import torch.jit
from typing import List, Tuple
csrc = """
#include <torch/extension.h>
#include <torch/script.h>

using namespace at;

Tensor test(std::vector<Tensor> inps) {  
  return inps[0] * 2; // not terribly safe!
}

static auto registry =
  torch::jit::RegisterOperators()
    .op("mytest::test", &test);

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("test", &test, "super test!");
}
"""

import torch.utils.cpp_extension

ext = torch.utils.cpp_extension.load_inline("test", [csrc], verbose=True,
                                            extra_ldflags=['-ltorch','-lcaffe2',
                                                           '-L'+os.path.join(os.path.dirname(torch._C.__file__), 'lib') ])
torch.ops.load_library(ext.__file__)

t = torch.randn(5)
print(torch.ops.mytest.test([t])) # works

@torch.jit.script
def test_wrapper(ts : List[torch.Tensor]): # need to do list!
    return torch.ops.mytest.test(ts)

print (test_wrapper([t])) # works

print (test_wrapper((t,))) # works

print ("doesn't work")

print (torch.jit.trace(test_wrapper, ((t,),)))  # doesn't work
# and I cannot be make it work


# the canonical way to do Tuples of arbitrary lengths (?)
@torch.jit.script
def test_wrapper2(ts : Tuple[torch.Tensor, ...]): # doesn't work
    return torch.ops.mytest.test(ts)
