RuntimeError:
Return value was annotated as having type Tensor but is actually of type Tuple[Tensor, Tensor]:
  File "/opt/anaconda3/lib/python3.8/site-packages/torch/nn/modules/pooling.py", line 227
    def forward(self, input: Tensor) -> Tensor:
        return F.max_pool3d(input, self.kernel_size, self.stride,
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            self.padding, self.dilation, self.ceil_mode,
                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            self.return_indices)
                            ~~~~~~~~~~~~~~~~~~~ <--- HERE