from pathlib import Path
import torch

model = torch.jit.load(Path("path/to/model.pth"))