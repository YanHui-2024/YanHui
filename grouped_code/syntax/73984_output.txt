graph = """
graph(%p1 : Long(requires_grad=0, device=cuda:0),
      %1 : Long(1, strides=[1], requires_grad=0, device=cuda:0),
      %p0 : int):
  %3 : int[] = prim::Constant[value=annotate(List[int], [])]()
  %6 : Long(requires_grad=0, device=cuda:0) = aten::reshape(%1, %3)
  %5 : Long(requires_grad=0, device=cuda:0) = aten::add(%6, %p1, %p0)
  return (%5)
"""
torch._C.parse_ir(graph)