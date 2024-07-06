import torch

ir = """
graph():
  %7 : Long(1, strides=[1], requires_grad=0, device=cpu) = prim::Constant[value={0}]()
  return (%7)
"""

torch._C.parse_ir(ir)