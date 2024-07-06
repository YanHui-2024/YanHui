graph(%num_iter : Long()) {
  %1 : Long() = onnx::Constant[value={1}]()
  %2 : Float(2, 2) = onnx::Constant[value= 1  1  1  1 [ CPUFloatType{2,2} ]]()
  %3 : Float(2, 1) = onnx::Constant[value= 1  1 [ CPUFloatType{2,1} ]]()
  %4 : Tensor = onnx::Loop(%num_iter, %1, %3)
    block0(%i : int, %cond : Tensor, %7 : Tensor) {
      %8 : Tensor = onnx::Mul(%2, %7)
      -> (%1, %8)
    }
  return (%2, %4);
}