Traceback (most recent call last):
  File "test_toy.py", line 67, in <module>
    e_losses += train_epoch(script_model, opt, criterion)
  File "test_toy.py", line 46, in train_epoch
    y_hat = model(x_batch)
  File "/scratch/wanchaol/local/pytorch/torch/nn/modules/module.py", line 491, in __call__
    result = self.forward(*input, **kwargs)
RuntimeError: bad optional access