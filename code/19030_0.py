class MyLayerPacked(torch.nn.Module):
    # same as before
    def __init__(self, original: MyLayer):
        self.packed_weight = self.__pack__(original.weight) # ByteTensor with pointer
    def forward(self, x):
        return torch.my_mm_fast(self.packed_weight, x)
    # it has to be script method to work in C++
    @torch.jit.script_method
    def __getstate__(self):
        return {'weight': torch.unpack_from_my_mm(self.packed_weight)}
    def __setstate__(self, state):
        # attribute mutability is required here
        self.packed_weight = torch.pack_for_my_mm(state['weight'])