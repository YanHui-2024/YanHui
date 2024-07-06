model_cpu = Architecture()
model_gpu = copy.deepcopy(model_cpu).to(torch.device("cuda"))

dummy_input = torch.randn(1, 3, 224, 224)

traced_model_cpu = torch.jit.trace(model_cpu, dummy_input)
traced_model_gpu = torch.jit.trace(model_gpu, dummy_input.to(torch.device('cuda')))