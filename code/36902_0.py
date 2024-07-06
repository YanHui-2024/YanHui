ERROR [0.008s]: test_class_sorting (jit.test_class_type.TestClassType)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\circleci\project\test\jit\test_class_type.py", line 394, in test_class_sorting
    self.checkScript(test, ([Foo(2), Foo(1), Foo(3)],))
  File "C:\Users\circleci\project\build\win_tmp\build\torch\testing\_internal\jit_utils.py", line 393, in checkScript
    frames_up=2)
  File "C:\Users\circleci\project\build\win_tmp\build\torch\testing\_internal\jit_utils.py", line 369, in checkScript
    cu = torch.jit.CompilationUnit(script, _frames_up=frames_up)
  File "C:\Users\circleci\project\build\win_tmp\build\torch\jit\__init__.py", line 1058, in __init__
    self.define(lang, _frames_up=_frames_up + 1)
  File "C:\Users\circleci\project\build\win_tmp\build\torch\jit\__init__.py", line 1063, in define
    self._c.define(lang, rcb)
RuntimeError: 
Expression of type tuple-literal cannot be used in a type expression:
  File "<string>", line 2
def test(li, reverse=False):
    # type: (List[Foo], bool) -> (List[int], List[int])
                                  ~~~~~~~~~~~~~~~~~~~ <--- HERE
    li_sorted = sorted(li)
    ret_sorted = torch.jit.annotate(List[int], [])