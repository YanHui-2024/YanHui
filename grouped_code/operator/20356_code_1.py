#include <torch/torch.h>

int main() {
  torch::Tensor tensor;
  torch::load(tensor, "tensor.pt");
  std::cout << tensor << std::endl;
}