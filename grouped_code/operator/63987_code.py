import torch
import io

class SparseTensorModule(torch.nn.Module):
	def __init__(self):
		super().__init__()
		self.a = torch.sparse.FloatTensor()

	def forward(self):
		pass

torch.jit.save(torch.jit.script(SparseTensorModule()), io.BytesIO())