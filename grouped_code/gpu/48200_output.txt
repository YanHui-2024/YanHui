Traceback (most recent call last):
  File "example.py", line 12, in <module>
    out = test(A).cpu().item()
RuntimeError: nvrtc: error: invalid value for --gpu-architecture (-arch)

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

extern "C" __global__
void func_1(float* t0, float* t1, float* aten_sub_flat) {
{
  if (512 * blockIdx.x + threadIdx.x<1000 ? 1 : 0) {
    float v = __ldg(t0 + (((512 * blockIdx.x + threadIdx.x) / 10) / 10) * 10 + (512 * blockIdx.x + threadIdx.x) % 10);
    float v_1 = __ldg(t1 + (512 * blockIdx.x + threadIdx.x) / 10);
    aten_sub_flat[512 * blockIdx.x + threadIdx.x] = v - v_1;
  }
}
}