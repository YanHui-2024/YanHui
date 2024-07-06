export MAX_JOBS=1

export PATH=/usr/local/cuda-10.0/bin:~/ccache/lib:$PATH
export CUDA_NVCC_EXECUTABLE=~/ccache/cuda/nvcc

export REL_WITH_DEB_INFO=1
export USE_CUDA=1
export TORCH_CUDA_ARCH_LIST=7.5

export BUILD_TEST=0
export BUILD_BINARY=0
export BUILD_CAFFE2_OPS=0
export USE_MKLDNN=0
export USE_FBGEMM=0
export USE_NNPACK=0
export USE_QNNPACK=0
export USE_XNNPACK=1
export USE_PYTORCH_QNNPACK=0

export USE_DISTRIBUTED=0
export USE_TENSORPIPE=0

pip install -e . -v