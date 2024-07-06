> terminate called after throwing an instance of 'torch::jit::script::ErrorReport'
>   what():  
> Lists must contain only a single type, expected: Float(1, 1083, 11) but found Float(1, 4332, 11) instead:
> op_version_set = 0
> def forward(self,
>     input_1: Tensor) -> Tensor:
>   _0 = [CONSTANTS.c0, CONSTANTS.c1, CONSTANTS.c2]
>        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ <--- HERE
>   return torch.cat(_0, 1)
> 
> Aborted (core dumped)