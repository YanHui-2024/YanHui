class MyJITModule(torch.jit.ScriptModule):
     def __init__(self):
         super(MyJITModule, self).__init__()
         self.lnorm = nn.LayerNorm([10, 10, 10])

     @torch.jit.script_method
     def forward(self, x):
         if self.training:
             self.training_code_only(x)
         return x

     def training_code_only(self, x):
         # do some torchscript incompatible logic
         arr = [1,2,3]
         for i, k in enumerate(arr):
             x[k] += x[k]

         return self.lnorm(x)


 print MyJITModule().graph
 MyJITModule().save("./conditional.pt")

graph(%x : Tensor
      %1 : Tensor) {
  %2 : bool = prim::Bool(%1)
   = prim::If(%2)
    block0() {
      %3 : () = ^training_code_only()(%x)
      -> ()
    }
    block1() {
      -> ()
    }
  return (%x);
}

RuntimeError:
could not export python function call training_code_only. Remove calls to python functions before export.:
@torch.jit.script_method
def forward(self, x):
    if self.training:
        self.training_code_only(x)
        ~~~~~~~~~~~~~ <--- HERE
    return x
