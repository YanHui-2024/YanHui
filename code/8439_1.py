graph(%0 : Float(5, 3, 224, 224)
      %1 : Float(32, 3, 9, 9)
      %2 : Float(32)
      %3 : Float(32)
      %4 : Float(32)) {
  %6 : Float(5, 3, 232, 232) = aten::reflection_pad2d[padding=[4, 4, 4, 4]](%0)
  %12 : Float(5, 32, 224, 224) = aten::_convolution[stride=[1, 1], padding=[0, 0], dilation=[1, 1], transposed=0, output_padding=[0, 0], groups=1, benchmark=0, deterministic=0, cudnn_enabled=1](%6, %1, %2)
  %51 : Dynamic = onnx::Constant[value=<Tensor>]()
  %52 : Dynamic = onnx::Constant[value=<Tensor>]()
  %53 : Float(5, 32, 224, 224) = onnx::InstanceNormalization[epsilon=1e-05](%12, %51, %52)
  return (%53);
}

Traceback (most recent call last):
  File "instance.py", line 29, in <module>
    traced(x)
  File "/Users/jamesreed/onnx-fairseq/pytorch/torch/nn/modules/module.py", line 468, in __call__
    result = self.forward(*input, **kwargs)
  File "/Users/jamesreed/onnx-fairseq/pytorch/torch/jit/__init__.py", line 690, in forward
    return self._get_method('forward')(*args, **kwargs)
RuntimeError: torch/csrc/jit/generated/aten_dispatch.cpp:13384: getDescriptor: Assertion `n->kind().is_aten()` failed: onnx::Constant is not an ATen op