USE_ASAN=1 USE_CUDA=0 python setup.py develop
LD_PRELOAD=/usr/lib64/libasan.so.4 python test/test_mobile_optimizer.py TestOptimizer.test_optimize_for_mobile_asan

// output tail: https://gist.github.com/vkuzo/7a0018b9e10ffe64dab0ac7381479f23