RuntimeError: isBoolList() INTERNAL ASSERT FAILED at ../aten/src/ATen/core/ivalue_inl.h:551, please report a bug to PyTorch. Expected BoolList but got GenericList
The above operation failed in interpreter, with the following stack trace:
at <string>:3:4
def bool_list(x):
    # type: (List[bool])
    x.clear()
    ~~~~~~~ <--- HERE