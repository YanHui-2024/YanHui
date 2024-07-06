import torch

class SomeModule(torch.jit.ScriptModule):

    @torch.jit.script_method
    def forward(self, x : torch.Tensor):
        bs = x.size(0)
        return bs + 1

example_outputs = (torch.LongTensor([SomeModule()(torch.rand(3, 4))]),)

import io
f = io.BytesIO()
torch.onnx._export(SomeModule(), (torch.rand(3, 4),), f, verbose=True, example_outputs=example_outputs)