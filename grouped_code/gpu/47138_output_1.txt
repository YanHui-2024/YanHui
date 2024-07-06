0
1
Traceback (most recent call last):
  File "repro.py", line 36, in <module>
    net(inp).mean().backward()
  File "/private/home/erikwijmans/miniconda3/envs/v4r/lib/python3.6/site-packages/torch/nn/modules/module.py", line 727, in _call_impl
    result = self.forward(*input, **kwargs)
RuntimeError: default_program(59): error: identifier "aten_add_flat__1" is undefined

default_program(60): error: no operator "=" matches these operands
            operand types are: half = float

2 errors detected in the compilation of "default_program".

nvrtc compilation failed: 

#define NAN __int_as_float(0x7fffffff)
#define POS_INFINITY __int_as_float(0x7f800000)
#define NEG_INFINITY __int_as_float(0xff800000)


template<typename T>
__device__ T maximum(T a, T b) {
  return isnan(a) ? a : (a > b ? a : b);
}

template<typename T>
__device__ T minimum(T a, T b) {
  return isnan(a) ? a : (a < b ? a : b);
}


#define __HALF_TO_US(var) *(reinterpret_cast<unsigned short *>(&(var)))
#define __HALF_TO_CUS(var) *(reinterpret_cast<const unsigned short *>(&(var)))
#if defined(__cplusplus)
  struct __align__(2) __half {
    __host__ __device__ __half() { }

  protected:
    unsigned short __x;
  };

  /* All intrinsic functions are only available to nvcc compilers */
  #if defined(__CUDACC__)
    /* Definitions of intrinsics */
    __device__ __half __float2half(const float f) {
      __half val;
      asm("{  cvt.rn.f16.f32 %0, %1;}\n" : "=h"(__HALF_TO_US(val)) : "f"(f));
      return val;
    }

    __device__ float __half2float(const __half h) {
      float val;
      asm("{  cvt.f32.f16 %0, %1;}\n" : "=f"(val) : "h"(__HALF_TO_CUS(h)));
      return val;
    }

  #endif /* defined(__CUDACC__) */
#endif /* defined(__cplusplus) */
#undef __HALF_TO_US
#undef __HALF_TO_CUS

typedef __half half;

extern "C" __global__
void func_1(half* t0, half* t1, half* t2, half* t3, half* aten_add_flat, half* aten_add_flat_1, half* aten_add_flat_2) {
{
  float t3_ = __half2float(t3[0]);
  float v = __half2float(t0[16 * ((512 * blockIdx.x + threadIdx.x) / 16) + (512 * blockIdx.x + threadIdx.x) % 16]);
  aten_add_flat_2[512 * blockIdx.x + threadIdx.x] = __float2half(v + t3_);
  float t2_ = __half2float(t2[0]);
  float t1_ = __half2float(t1[0]);
  float aten_add_flat_ = __half2float(aten_add_flat_1[512 * blockIdx.x + threadIdx.x]);
  aten_add_flat__1 = __float2half((__half2float(t0[16 * ((512 * blockIdx.x + threadIdx.x) / 16) + (512 * blockIdx.x + threadIdx.x) % 16]) + t3_) * t2_ + t1_);
  aten_add_flat_1[512 * blockIdx.x + threadIdx.x] = aten_add_flat_;
  float v_1 = __half2float(t0[16 * ((512 * blockIdx.x + threadIdx.x) / 16) + (512 * blockIdx.x + threadIdx.x) % 16]);
  float v_2 = __half2float(t0[16 * ((512 * blockIdx.x + threadIdx.x) / 16) + (512 * blockIdx.x + threadIdx.x) % 16]);
  float v_3 = __half2float(t0[16 * ((512 * blockIdx.x + threadIdx.x) / 16) + (512 * blockIdx.x + threadIdx.x) % 16]);
  aten_add_flat[512 * blockIdx.x + threadIdx.x] = __float2half(((v_1 + t3_) * t2_ + t1_) * ((v_2 + t3_) * t2_ + t1_) + v_3);
}
}