> RuntimeError: 
> arguments for call are not valid:
>   
>   for operator aten::__interpolate(Tensor input, int? size=<default>, float[]? scale_factor=<default>, string mode=<default>, bool? align_corners=<default>) -> Tensor:
>   expected a value of type float[]? for argument 'scale_factor' but found int
>   @weak_script_method
>   def forward(self, input):
>       warnings.warn("nn.{} is deprecated. Use nn.functional.interpolate instead.".format(self.name))
>       return F.interpolate(input, self.size, self.scale_factor, self.mode, self.align_corners)
>                                              ~~~~~~~~~~ <--- HERE
>   
>   for operator aten::__interpolate(Tensor input, int[]? size=<default>, float[]? scale_factor=<default>, string mode=<default>, bool? align_corners=<default>) -> Tensor:
>   expected a value of type float[]? for argument 'scale_factor' but found int
>   @weak_script_method
>   def forward(self, input):
>       warnings.warn("nn.{} is deprecated. Use nn.functional.interpolate instead.".format(self.name))
>       return F.interpolate(input, self.size, self.scale_factor, self.mode, self.align_corners)
>                                              ~~~~~~~~~~ <--- HERE
>   
>   for operator aten::__interpolate(Tensor input, int? size=<default>, float? scale_factor=<default>, string mode=<default>, bool? align_corners=<default>) -> Tensor:
>   expected a value of type float? for argument 'scale_factor' but found int
>   @weak_script_method
>   def forward(self, input):
>       warnings.warn("nn.{} is deprecated. Use nn.functional.interpolate instead.".format(self.name))
>       return F.interpolate(input, self.size, self.scale_factor, self.mode, self.align_corners)
>                                              ~~~~~~~~~~ <--- HERE
>   
>   for operator aten::__interpolate(Tensor input, int[]? size=<default>, float? scale_factor=<default>, string mode=<default>, bool? align_corners=<default>) -> Tensor:
>   expected a value of type float? for argument 'scale_factor' but found int
>   @weak_script_method
>   def forward(self, input):
>       warnings.warn("nn.{} is deprecated. Use nn.functional.interpolate instead.".format(self.name))
>       return F.interpolate(input, self.size, self.scale_factor, self.mode, self.align_corners)
>                                              ~~~~~~~~~~ <--- HERE
> for call at:
> @weak_script_method
> def forward(self, input):
>     warnings.warn("nn.{} is deprecated. Use nn.functional.interpolate instead.".format(self.name))
>     return F.interpolate(input, self.size, self.scale_factor, self.mode, self.align_corners)
>            ~~~~~~~~~~~~~ <--- HERE

and the traceback is:

> Traceback (most recent call last):
>   File "train.py", line 204, in <module>
>     main()
>   File "train.py", line 80, in main
>     model = YOLOv3(anchors, anch_mask, n_classes, ignore_thre=ignore_thre)
>   File "/home/.conda/envs/python36_ocv_pytorch/lib/python3.6/site-packages/torch/jit/__init__.py", line 951, in init_then_register
>     original_init(self, *args, **kwargs)
>   File "/home/Documents/yolotorch/training_implementation/models/yolov3.py", line 294, in __init__
>     self.module_list= create_yolov3_modules(anchors, anch_mask, n_classes, ignore_thre)
>   File "/home/.conda/envs/python36_ocv_pytorch/lib/python3.6/site-packages/torch/jit/__init__.py", line 1123, in __setattr__
>     super(ScriptModule, self).__setattr__(attr, _ConstModuleList(value))
>   File "/home/.conda/envs/python36_ocv_pytorch/lib/python3.6/site-packages/torch/jit/__init__.py", line 951, in init_then_register
>     original_init(self, *args, **kwargs)
>   File "/home/.conda/envs/python36_ocv_pytorch/lib/python3.6/site-packages/torch/jit/__init__.py", line 1355, in __init__
>     module = _make_strong(module)
>   File "/home/.conda/envs/python36_ocv_pytorch/lib/python3.6/site-packages/torch/jit/__init__.py", line 1254, in _make_strong
>     proxy = WeakScriptModuleProxy(mod, stubs)
>   File "/home/.conda/envs/python36_ocv_pytorch/lib/python3.6/site-packages/torch/jit/__init__.py", line 951, in init_then_register
>     original_init(self, *args, **kwargs)
>   File "/home/.conda/envs/python36_ocv_pytorch/lib/python3.6/site-packages/torch/jit/__init__.py", line 1191, in __init__
>     _create_methods_from_stubs(self, stubs)
>   File "/home/.conda/envs/python36_ocv_pytorch/lib/python3.6/site-packages/torch/jit/__init__.py", line 913, in _create_methods_from_stubs
>     self._create_methods(defs, rcbs, defaults)