    std::vector<c10::IValue> input;
    for (size_t pos = 0; pos < input_data.size(); ++pos)
    {
        c10::ivalue::DictUnorderedMap<c10::IValue, c10::IValue> ivalue_map;
        for (auto x: input_data[pos])
        {
            c10::IValue key = x.first;
            c10::IValue value = x.second.to(device_);
            ivalue_map[key] = value;
        }
        c10::IValue map_as_ivalue = ivalue_map;
        input.push_back(map_as_ivalue);
    }
    auto arg_index = schema.argumentIndexWithName(input_name);
    std::vector<torch::jit::IValue> inputs_;
    inputs_.at(arg_index.value()) = input;