Traceback (most recent call last):
  File "dank.py", line 15, in <module>
    ''')
  File "/Users/jamesreed/onnx-fairseq/pytorch/torch/jit/__init__.py", line 566, in __init__
    self.define(lang, _frames_up=_frames_up + 1)
  File "/Users/jamesreed/onnx-fairseq/pytorch/torch/jit/__init__.py", line 572, in define
    self.module._define(lang, rcb, False)
RuntimeError: expected ident but found 'elif' here:

def fizzbuzz(niter : int):
    for i in range(niter):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
        ~~~~ <--- HERE
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
    return niter