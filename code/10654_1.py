import torch
import torch.nn as nn
from torch.jit import trace
class test(nn.Module):
        def __init__(self):
                super(test, self).__init__()
                self.conv = nn.Conv2d(1, 32, kernel_size=3,padding=1)

        def forward(self, x):
                y = self.conv(x)
                w = nn.functional.interpolate(y, mode='bilinear', align_corners=False, scale_factor=0.5)
                return w

f=test()
x = torch.zeros(1,1,28,28)
ret = trace(x)(f)

RuntimeError                              Traceback (most recent call last)
<ipython-input-1-65fe10b64581> in <module>()
     14 f=test()
     15 x = torch.zeros(1,1,28,28)
---> 16 ret = trace(x)(f)

~/nn/pytorch/lib/python3.6/site-packages/torch/jit/__init__.py in wrapper(func)
    288 
    289         module = TopLevelTracedModule(func, **executor_options)
--> 290         module._create_method_from_trace('forward', func, args)
    291         return module
    292 

~/nn/pytorch/lib/python3.6/site-packages/torch/nn/modules/module.py in __call__(self, *input, **kwargs)
    473             hook(self, input)
    474         if torch._C._get_tracing_state():
--> 475             result = self._slow_forward(*input, **kwargs)
    476         else:
    477             result = self.forward(*input, **kwargs)

~/nn/pytorch/lib/python3.6/site-packages/torch/nn/modules/module.py in _slow_forward(self, *input, **kwargs)
    463         tracing_state._traced_module_stack.append(self)
    464         try:
--> 465             result = self.forward(*input, **kwargs)
    466         finally:
    467             tracing_state.pop_scope()

<ipython-input-1-65fe10b64581> in forward(self, x)
      9         def forward(self, x):
     10                 y = self.conv(x)
---> 11                 w = nn.functional.interpolate(y, mode='bilinear', align_corners=False, scale_factor=0.5)
     12                 return w
     13 
~/nn/pytorch/lib/python3.6/site-packages/torch/nn/functional.py in interpolate(input, size, scale_factor, mode, align_corners)
   2069         raise NotImplementedError("Got 4D input, but linear mode needs 3D input")
   2070     elif input.dim() == 4 and mode == 'bilinear':
-> 2071         return torch._C._nn.upsample_bilinear2d(input, _output_size(2), align_corners)
   2072     elif input.dim() == 4 and mode == 'trilinear':
   2073         raise NotImplementedError("Got 4D input, but trilinear mode needs 5D input")

RuntimeError: invalid argument 2: input and output sizes should be greater than 0, but got input (H: 28, W: 28) output (H: 0, W: 0) at /home/disk0/.pytorch/pytorch/aten/src/THNN/generic/SpatialUpSamplingBilinear.c:19