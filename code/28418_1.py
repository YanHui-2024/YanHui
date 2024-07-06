Traceback (most recent call last):
  File "test.py", line 4, in <module>
    torch.jit.script(nn.RNN(32, 64, 1))
  File "/opt/anaconda/envs/test/lib/python3.6/site-packages/torch/jit/__init__.py", line 1203, in script
    return torch.jit.torch.jit._recursive.recursive_script(obj)
  File "/opt/anaconda/envs/test/lib/python3.6/site-packages/torch/jit/_recursive.py", line 173, in recursive_script
    return copy_to_script_module(mod, overload_stubs + stubs)
  File "/opt/anaconda/envs/test/lib/python3.6/site-packages/torch/jit/_recursive.py", line 95, in copy_to_script_module
    torch.jit._create_methods_from_stubs(script_module, stubs)
  File "/opt/anaconda/envs/test/lib/python3.6/site-packages/torch/jit/__init__.py", line 1423, in _create_methods_from_stubs
    self._c._create_methods(self, defs, rcbs, defaults)
RuntimeError: 
Tensor cannot be used as a tuple:
at /opt/anaconda/envs/test/lib/python3.6/site-packages/torch/nn/modules/rnn.py:184:67
    def forward(self, input, hx=None):
        is_packed = isinstance(input, PackedSequence)
        if is_packed:
            input, batch_sizes, sorted_indices, unsorted_indices = input
                                                                   ~~~~~ <--- HERE
            max_batch_size = batch_sizes[0]
            max_batch_size = int(max_batch_size)
        else:
            batch_sizes = None
            max_batch_size = input.size(0) if self.batch_first else input.size(1)
            sorted_indices = None
            unsorted_indices = None

        if hx is None: