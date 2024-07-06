(gdb) f 9
#9  0x00007fffcdeb2127 in torch::jit::(anonymous namespace)::<lambda(torch::jit::Stack&)>::operator()(torch::jit::Stack &) const (__closure=0x44ba5580, 
    stack=std::vector of length 2, capacity 2 = {...}) at /home/stefan/pytorch/torch/csrc/jit/generated/register_aten_ops_1.cpp:2948
2948              );
(gdb) f 8
#8  0x00007fffcde9aa4d in at::adaptive_max_pool2d (self=..., output_size=...) at /home/stefan/pytorch/build/aten/src/ATen/Functions.h:5728
5728        return detail::infer_type(self).adaptive_max_pool2d(self, output_size);
(gdb) p output_size.size()
$1 = 1