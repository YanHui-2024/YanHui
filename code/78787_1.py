graph(%a.1 : Tensor,
      %b.1 : Tensor):
  %4 : NoneType = prim::Constant()
  %c.1 : Tensor = aten::repeat_interleave(%b.1, %4) # /data/users/dberard/scripts/oncall/repeat-interleave.py:6:8
  %9 : Tensor[] = prim::ListConstruct(%c.1, %a.1, %b.1)
  return (%9)