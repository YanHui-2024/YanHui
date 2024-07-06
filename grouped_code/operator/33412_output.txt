  input_tensor = torch.range(20, 80)
graph(%data : Float(61)):
  %1 : Float(61), %2 : Long(61) = onnx::TopK[axis=-1, k=61](%data) # onnx.py:10:0
  return (%2)