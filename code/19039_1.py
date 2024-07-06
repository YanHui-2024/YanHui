#include <torch/script.h>

#include <memory>

int main() {
    std::shared_ptr<torch::jit::script::Module> module = torch::jit::load("/tmp/bn_gpu.pt");
    module->to(torch::kCPU);

    std::vector<torch::jit::IValue> inputs;
    inputs.emplace_back(torch::randn({6, 10}));
    auto output = module->forward(inputs).toTensor();
}