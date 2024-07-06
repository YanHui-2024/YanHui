def foo() -> Tuple[List[int], List[int]]:
  a = [1, 2, 3]
  b = torch.list(a)
  _0 = torch.pop(a, -1)
  return (a, b)

actual ([1, 2], [1, 2])
expected ([1, 2], [1, 2, 3])
graph():
  %3 : int = prim::Constant[value=3]() # list_repro.py:4:16
  %2 : int = prim::Constant[value=2]() # list_repro.py:4:13
  %1 : int = prim::Constant[value=1]() # list_repro.py:4:10
  %0 : int = prim::Constant[value=-1]()
  %a.1 : int[] = prim::ListConstruct(%1, %2, %3)
  %b.1 : int[] = aten::list(%a.1) # list_repro.py:5:9
  %6 : int = aten::pop(%a.1, %0) # list_repro.py:6:5
  %7 : (int[], int[]) = prim::TupleConstruct(%a.1, %b.1)
  return (%7)