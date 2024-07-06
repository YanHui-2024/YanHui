torch.jit.save(traced_model_cpu, "model_cpu.pth")
torch.jit.save(traced_model_gpu, "model_gpu.pth")

traced_model_cpu_loaded = torch.jit.load("model_cpu.pth")
traced_model_gpu_loaded = torch.jit.load("model_gpu.pth")