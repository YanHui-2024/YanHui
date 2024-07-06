raceback (most recent call last):
  File "/home/chenyufei/Development/nn-parser/local_scripts/pytorch_1_2_master_bug.py", line 14, in <module>
    print(m)
  File "/home/chenyufei/.local/anaconda3.7/lib/python3.7/site-packages/torch/nn/modules/module.py", line 1044, in __repr__
    mod_str = repr(module)
  File "/home/chenyufei/.local/anaconda3.7/lib/python3.7/site-packages/torch/nn/modules/module.py", line 1038, in __repr__
    extra_repr = self.extra_repr()
  File "/home/chenyufei/.local/anaconda3.7/lib/python3.7/site-packages/torch/nn/modules/normalization.py", line 161, in extra_repr
    'elementwise_affine={elementwise_affine}'.format(**self.__dict__)
KeyError: 'elementwise_affine'