import torch

net = torch.nn.Identity()
x = torch.tensor([1, 2, 3])

# these two lines create warnings in PyCharm (i.e. example_inputs=x and args=x are highlighted in yellow
# and the code inspection lists the warnings "Expected type 'tuple',  got 'Tensor' instead")
torch.jit.trace(func=net, example_inputs=x)
torch.onnx.export(model=net, args=x, f="test.onnx")

# these two don't
torch.jit.trace(func=net, example_inputs=(x,))
torch.onnx.export(model=net, args=(x,), f="test2.onnx")