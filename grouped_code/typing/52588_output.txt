[tensor([[4., 4.],
        [4., 4.]]), tensor([[4., 4., 4.],
        [4., 4., 4.],
        [4., 4., 4.]]), tensor([[4., 4., 4., 4.],
        [4., 4., 4., 4.],
        [4., 4., 4., 4.],
        [4., 4., 4., 4.]])]
RecursiveScriptModule(
  original_name=Sequential
  (0): RecursiveScriptModule(original_name=ModelWithInputAsListOfTensor)
  (1): RecursiveScriptModule(original_name=ModelWithInputAsListOfTensor)
)
---------------------
Traceback (most recent call last):
  File "tests/test_seq.py", line 32, in <module>
    res = scripted_model(test_input)
  File "/Users/linus/anaconda3/lib/python3.7/site-packages/torch/nn/modules/module.py", line 727, in _call_impl
    result = self.forward(*input, **kwargs)
RuntimeError: forward() Expected a value of type 'Tensor (inferred)' for argument 'input' but instead found type 'list'.
Inferred 'input' to be of type 'Tensor' because it was not annotated with an explicit type.
Position: 1
Value: [tensor([[1., 1.],
        [1., 1.]]), tensor([[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]]), tensor([[1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.]])]
Declaration: forward(__torch__.torch.nn.modules.container.Sequential self, Tensor input) -> (Tensor[])
Cast error details: Unable to cast Python instance to C++ type (compile in debug mode for details)