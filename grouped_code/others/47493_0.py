// test.cu
#include <torch/extension.h>

bool is_installed() { return true; }

TORCH_LIBRARY(my_ops, m) {
  m.def("is_installed() -> bool", &is_installed);
}