import os
import torch
import torch.jit
csrc = """
#include <torch/extension.h>
#include <torch/script.h>

using namespace at;

Tensor test(const Tensor& inp) {
  return inp * 2;
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
print(torch.ops.mytest.test(t)) # works

@torch.jit.script
def test_wrapper(t):
    return torch.ops.mytest.test(t)

print (torch.jit.trace(test_wrapper, (t,)))  # works, too


print (torch.jit.trace(torch.ops.mytest.test, (t,)))  # should work!