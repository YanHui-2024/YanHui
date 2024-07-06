auto model = torch::jit::load("model.pt");
const int prediction_horizon_s = model.get_attribute("prediction_horizon_s");