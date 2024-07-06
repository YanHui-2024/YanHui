import torch

with torch.package.PackageExporter("output") as e:
    e.save_source_string('m',  '__import__("these", dont, have, to, be, contants)')