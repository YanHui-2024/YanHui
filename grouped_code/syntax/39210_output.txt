File ".../lib/python3.7/site-packages/torch/jit/_recursive.py", line 279, in create_methods_from_stubs
    concrete_type._create_methods(defs, rcbs, defaults)
RuntimeError:
Tried to access nonexistent attribute or method 'index' of type 'List[str]'.:
  File "test.py", line 11
    def forward(self, s: str, l: List[str]):
        return l.index(s)
               ~~~~~~~ <--- HERE