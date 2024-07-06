Arguments for call are not valid.
The following variants are available:
  
  aten::hash.str(str t) -> (int):
  Expected a value of type 'str' for argument 't' but instead found type 'Tuple[int]'.
  
  aten::hash.int(int t) -> (int):
  Expected a value of type 'int' for argument 't' but instead found type 'Tuple[int]'.
  
  aten::hash.float(float t) -> (int):
  Expected a value of type 'float' for argument 't' but instead found type 'Tuple[int]'.

The original call is:
  File "<ipython-input-63-fad4df6d9cb7>", line 11
    def forward(self, ids: Tuple[int]) -> int:
        return hash(ids)
               ~~~~ <--- HERE