python test.py
Traceback (most recent call last):
  File "test.py", line 43, in <module>
    x, xs = model.forward(torch.ones(10, 10), {})
RuntimeError: The following operation failed in the TorchScript interpreter.
Traceback of TorchScript (most recent call last):
  File "test.py", line 36, in forward
            x = torch.cat((x, score), dim=1)  # removing this line makes it work
        else:
            x, meta = self.activation(x, meta)
                      ~~~~~~~~~~~~~~~ <--- HERE
        meta["meta_y_hat"] = x  # removing this line makes it work
        return meta["meta_y_hat"], meta
  File "test.py", line 13, in forward
        meta["meta_y_hat"] = x
        # return x, meta # would make it work
        return meta["meta_y_hat"], meta  # JIT claims it errors here
               ~~~~~~~~~~~~~~~~~ <--- HERE
RuntimeError: KeyError: meta_y_hat