orig_module = torch.jit.script(MyModel())   # or trace, or load
frozen_module = torch.jit.freeze(orig_module)   # In current PR torch._C._freeze_module(orig_module)
print(orig_module.weight) # Works
expect_throw(print(frozen_module.weight)) # Fails because all attributes are removed