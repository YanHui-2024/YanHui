TypeError                                 Traceback (most recent call last)
Input In [87], in <cell line: 16>()
     13         self.names_ages["someone"] = 20
     14         assert isinstance(self.names_ages["someone"], int)
---> 16 m = AttributeModule()

Input In [87], in AttributeModule.__init__(self)
      7 self.foo = torch.jit.Attribute(0.1, float)
      9 # we should be able to use self.foo as a float here
---> 10 assert 0.0 < self.foo
     12 self.names_ages = torch.jit.Attribute({}, Dict[str, int])
     13 self.names_ages["someone"] = 20

TypeError: '<' not supported between instances of 'float' and 'Attribute'