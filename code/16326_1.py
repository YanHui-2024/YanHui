    std::string path = "./model.pt";
    std::shared_ptr<torch::jit::script::Module> module = torch::jit::load(path);

    std::vector<torch::Tensor> one_frame = {
            torch::rand({4, 4}),
            torch::rand({4, 4}),
            torch::rand({4, 4}),
            torch::rand({4, 4}),

    };

    std::vector<torch::jit::IValue> frames;
    frames.push_back(one_frame);
    frames.push_back(one_frame);
    std::vector<torch::jit::IValue> inputs;
    inputs.push_back(frames);

    auto result = module->forward(inputs);
    log_info("finished inference")
