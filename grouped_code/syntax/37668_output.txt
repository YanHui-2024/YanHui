RuntimeError: 
Tried to access nonexistent attribute or method 'p1' of type 'Tuple[float, int]'.:
  File "test_torch_script.py", line 72
    def forward(self):
        print(self.params.p1)
              ~~~~~~~~~~~~~~ <--- HERE