17:20:04 ~ $ python dropoutcrash.py
Traceback (most recent call last):
  File "dropoutcrash.py", line 9, in <module>
    dropout_test(torch.zeros(1, 2, 3, requires_grad=True))
RuntimeError:
VariableType::ID() not implemented:
operation failed in interpreter:
/Users/jamesreed/onnx-fairseq/pytorch/torch/nn/functional.py(555): dropout
dropoutcrash.py(7): dropout_test
/Users/jamesreed/onnx-fairseq/pytorch/torch/jit/__init__.py(475): wrapper
dropoutcrash.py(4): <module>