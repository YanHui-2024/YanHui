compile,58,RuntimeError: python value of type 'str' cannot be used as a value:,"RuntimeError: 
python value of type 'str' cannot be used as a value:
  File ""/tmp/paritybenchydc_9oju/pbg51yh9q6.py"", line 51
    def forward(self, x):
        x = functional.batch_norm(x, self.running_mean, self.running_var, self.weight, self.bias, self.training, self.momentum, self.eps)
        if self.activation == ACT_RELU:
                              ~~~~~~~~ <--- HERE
            return functional.relu(x, inplace=True)
        elif self.activation == ACT_LEAKY_RELU: