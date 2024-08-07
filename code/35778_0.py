In [1]: import torch                                                                                                                 

In [2]: import torch.utils.collect_env                                                                                               

In [3]: torch.utils.collect_env.main()                                                                                               
Collecting environment information...
PyTorch version: 1.5.0+cpu
Is debug build: No
CUDA used to build PyTorch: None

OS: Fedora release 30 (Thirty)
GCC version: (GCC) 9.1.1 20190503 (Red Hat 9.1.1-1)
CMake version: version 3.14.4

Python version: 3.7
Is CUDA available: No
CUDA runtime version: No CUDA
GPU models and configuration: No CUDA
Nvidia driver version: No CUDA
cuDNN version: No CUDA

Versions of relevant libraries:
[pip3] numpy==1.17.0
[pip3] pytorch-pretrained-bert==0.6.2
[pip3] torch==1.5.0+cpu
[pip3] torchtext==0.4.0
[pip3] torchvision==0.6.0.dev20200226+cpu
[conda] Could not collect

In [4]: @torch.jit.script 
   ...: def f(): 
   ...:     return None 
   ...:                                                                                                                              

In [5]: node = list(f.graph.nodes())[0]                                                                                              

In [6]: t = node.outputsAt(0).type()                                                                                                                           

In [7]: print(t)                                                                                                                                               
None

In [8]: print(str(t))                                                                                                                                          
None

In [9]: print(repr(t))                                                                                                                                         
None

In [10]: print(type(t))                                                                                                                                        
<class 'torch._C.NoneType'>

In [11]: # Hrm.  It's not really None.                                                                                                                         

In [12]: t is None                                                                                                                                             
Out[12]: False

In [13]: t == None                                                                                                                                             
Segmentation fault (core dumped)