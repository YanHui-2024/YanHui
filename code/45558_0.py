terminate called after throwing an instance of 'c10::Error'
  what():  isTensor() INTERNAL ASSERT FAILED at "/home/huaidong.xhd/libtorch/include/ATen/core/ivalue_inl.h":126, please report a bug to PyTorch. Expected Tensor but got None
Exception raised from toTensor at /home/huaidong.xhd/libtorch/include/ATen/core/ivalue_inl.h:126 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x3e (0x7f1744327dee in /home/huaidong.xhd/libtorch/lib/libc10.so)
frame #1: c10::IValue::toTensor() && + 0xb5 (0x405cdd in /home/huaidong.xhd/Documents/git/develop/ml-predict-service/build/a.out)
frame #2: /home/huaidong.xhd/Documents/git/develop/ml-predict-service/build/a.out() [0x403aba]
frame #3: __libc_start_main + 0xf5 (0x7f173cd2c555 in /lib64/libc.so.6)
frame #4: /home/huaidong.xhd/Documents/git/develop/ml-predict-service/build/a.out() [0x4036e9]