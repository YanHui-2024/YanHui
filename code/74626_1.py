Traceback (most recent call last):
  File "repro.py", line 16, in <module>
    a = AttributeModule()
  File "repro.py", line 10, in __init__
    assert 0.0 < self.foo
TypeError: '<' not supported between instances of 'float' and 'Attribute'