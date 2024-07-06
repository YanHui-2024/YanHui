  std::ifstream in("/tmp/s.pt");
  auto m = torch::jit::load(in);
  auto cloned = m.clone();