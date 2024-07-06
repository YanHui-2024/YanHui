#include "torch/jit.h"

int main() {

  const auto text = R"(
def a(x, y=1):
    print("a1")
    print("a2")
    return x
  )";

  torch::jit::compile(text);
  return 0;
}