Traceback (most recent call last):
  File "/Users/suo/scratch/test.py", line 64, in <module>
    f = Foo(BoundingBoxList(torch.rand(3, 4), (2, 3), "xyxy"))
  File "/Users/suo/pytorch/torch/jit/__init__.py", line 1178, in init_then_register
    original_init(self, *args, **kwargs)
  File "/Users/suo/scratch/test.py", line 57, in __init__
    self.words = torch.jit.Attribute(bbox, BoundingBoxList)
  File "/Users/suo/pytorch/torch/jit/__init__.py", line 1377, in __setattr__
    the_type = torch.jit.annotations.ann_to_type(value.type)
  File "/Users/suo/pytorch/torch/jit/annotations.py", line 184, in ann_to_type
    raise ValueError("Unknown type annotation: '{}'".format(ann.__name__))
ValueError: Unknown type annotation: 'BoundingBoxList'