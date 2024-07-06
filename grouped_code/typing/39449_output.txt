RuntimeError: 
all inputs of range must be ints, found Tensor in argument 0:
  File "<ipython-input-13-8c4279680b35>", line 2
def foo(x: torch.Tensor, y):  # Missing "y: int"
    for _ in range(y):
             ~~~~~~~ <--- HERE
        x = x + 1
    return x