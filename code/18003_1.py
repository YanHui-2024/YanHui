auto module = torch::jit::load("./ModelThatNeedsDebugging.pt");
module->forward(input);