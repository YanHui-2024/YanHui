from __future__ import print_function
import torch
import onnx
from onnx.onnx_pb2 import TensorProto

class SimpleModel(torch.jit.ScriptModule):
    def __init__(self):
        super(SimpleModel, self).__init__()
        #self.xx = torch.zeros(2, 2)

    @torch.jit.script_method
    def forward(self, num_iter : int):
        x = torch.ones([2, 2], dtype=torch.float32)
        y = torch.ones(2, 2, dtype=torch.float32)
        v = torch.ones(2, 1, dtype=torch.float32)
        for i in range(num_iter):
            v = x * v
        return x, v

model = SimpleModel()

model_onnx = torch.onnx._export(model, torch.tensor(5), "simple_loop.onnx",
        verbose=True,
        operator_export_type=torch.onnx.OperatorExportTypes.ONNX,
        example_outputs=(torch.zeros(2,2), torch.zeros(2,1)))

prog = onnx.load("simple_loop.onnx")
print("%1 tensor type is int64? ", prog.graph.node[0].attribute[0].t.data_type
        == TensorProto.INT64)