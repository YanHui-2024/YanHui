
/home/david/Documents/GitHub/cleanoc/cleanrl/ppo_lngru_jit.py:281: UserWarning: FALLBACK path has been taken inside: compileCudaFusionGroup. This is an indication that codegen Failed for some reason.
To debug try disable codegen fallback path via setting the env variable `export PYTORCH_NVFUSER_DISABLE=fallback`
To report the issue, try enable logging via setting the envvariable ` export PYTORCH_JIT_LOG_LEVEL=manager.cpp`
 (Triggered internally at  /opt/conda/conda-bld/pytorch_1656352657443/work/torch/csrc/jit/codegen/cuda/manager.cpp:237.)
  next_gru_state = agent.get_next_state(next_obs, next_gru_state, next_done, prev_actions[step])
/home/david/Documents/GitHub/cleanoc/cleanrl/ppo_lngru_jit.py:281: UserWarning: FALLBACK path has been taken inside: runCudaFusionGroup. This is an indication that codegen Failed for some reason.
To debug try disable codegen fallback path via setting the env variable `export PYTORCH_NVFUSER_DISABLE=fallback`
 (Triggered internally at  /opt/conda/conda-bld/pytorch_1656352657443/work/torch/csrc/jit/codegen/cuda/manager.cpp:329.)
  next_gru_state = agent.get_next_state(next_obs, next_gru_state, next_done, prev_actions[step])
Traceback (most recent call last):
  File "/home/david/Documents/GitHub/cleanoc/cleanrl/ppo_lngru_jit.py", line 281, in <module>
    next_gru_state = agent.get_next_state(next_obs, next_gru_state, next_done, prev_actions[step])
RuntimeError: The following operation failed in the TorchScript interpreter.
Traceback of TorchScript (most recent call last):
RuntimeError: The following operation failed in the TorchScript interpreter.
Traceback of TorchScript (most recent call last):
RuntimeError: Expected weight to be of same shape as normalized_shape, but got weight of shape [4, 128] and normalized_shape = [384]