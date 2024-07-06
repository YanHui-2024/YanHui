graph(%0 : Float(2, 3, 5, strides=[15, 5, 1], requires_grad=0, device=cpu)):
  %1 : Long(3, strides=[1], device=cpu) = onnx::Shape(%0)
  %2 : Long(device=cpu) = onnx::Constant[value={1}]()
  %3 : Long(device=cpu) = onnx::Gather[axis=0](%1, %2) # test/onnx/test_m.py:38:0
  %4 : Long(requires_grad=0, device=cpu) = onnx::Constant[value={2}]()
  %5 : Long(requires_grad=0, device=cpu) = onnx::Add(%3, %4) # test/onnx/test_m.py:40:0
  %6 : Long(requires_grad=0, device=cpu) = onnx::Add(%5, %5) # test/onnx/test_m.py:41:0   ===> %5 proves that both seq_length and real_seq_length have same values/memory
  return (%6)