Traceback (most recent call last):
  File "/Users/scripts/torchscript_bug.py", line 24, in <module>
    out = torch.jit.script(pad)
  File "/usr/local/Caskroom/miniforge/base/envs/ludwig/lib/python3.9/site-packages/torch/jit/_script.py", line 1341, in script
    fn = torch._C._jit_script_compile(
  File "/usr/local/Caskroom/miniforge/base/envs/ludwig/lib/python3.9/site-packages/torch/jit/annotations.py", line 366, in try_ann_to_type
    assert maybe_type, msg.format(repr(ann), repr(maybe_type))
AssertionError: Unsupported annotation typing.Union[int, tuple[int, int]] could not be resolved because None could not be resolved.