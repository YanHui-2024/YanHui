---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-43405c9b8ee8> in <module>()
----> 1 print features

/.../lib/python2.7/site-packages/torch/tensor.pyc in __repr__(self)
     67         else:
     68             if hasattr(sys.stdout, 'encoding'):
---> 69                 return torch._tensor_str._str(self).encode(
     70                     sys.stdout.encoding or 'UTF-8', 'replace')
     71             else:

/.../lib/python2.7/site-packages/torch/_tensor_str.pyc in _str(self)
    283         name = type(self.grad_fn).__name__
    284         if name == 'CppFunction':
--> 285             name = self.grad_fn.name().rsplit('::', maxsplit=1)[-1]
    286         suffixes.append('grad_fn=<{}>'.format(name))
    287     elif self.requires_grad:

TypeError: rsplit() takes no keyword arguments