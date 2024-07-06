RuntimeError: 
Tried to access nonexistent attribute or method 'name' of type '__torch__.Params'.:
  File "test_torch_script.py", line 72
    def forward(self, params: Params):
        print(params.name)
              ~~~~~~~~~~~ <--- HERE