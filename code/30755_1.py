RuntimeError:
Tried to access nonexistent attribute or method '__add__' of type '__torch__.M'. Did you forget to initialize an attribute in __init__()?:
  File "/private/home/suo/scratch/test.py", line 21
    @staticmethod
    def some_method(x):
        return x + 10
               ~~~~~~ <--- HERE
'M.some_method' is being compiled since it was called from 'M.forward'
  File "/private/home/suo/scratch/test.py", line 24
    def forward(self, x):
        return self.some_method(x)
               ~~~~~~~~~~~~~~~~~~ <--- HERE