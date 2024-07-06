import torch
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=1) as executor:
    executor.submit(torch.jit.load, 'dummy_model.pt')