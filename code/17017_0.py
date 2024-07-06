#include <torch/csrc/jit/custom_operator.h>

torch::Tensor new_string_op(vector<string> input, torch::Tensor warp) {

  torch::Tensor output = torch::from_blob(warp.ptr<float>(), /*sizes=*/{8, 8});
  return output.clone();
}

static auto registry =
  torch::jit::RegisterOperators("my_ops::new_string_op", &new_string_op)