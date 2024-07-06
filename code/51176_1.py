RuntimeError:
lhs of assignment must be a variable, subscript, or starred expression:
  File "self_attr.py", line 8
    def __init__(self, a: int, b: int):
        self.a, self.b = pass_through(a, b)
        ~~~~~~ <--- HERE