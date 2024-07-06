Fatal Python error: Segmentation fault

Current thread 0x00007f054a514740 (most recent call first):
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/_io/saferepr.py", line 58 in repr_instance
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/reprlib.py", line 62 in repr1
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/reprlib.py", line 52 in repr
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/_io/saferepr.py", line 49 in repr
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/_io/saferepr.py", line 88 in saferepr
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/_code/code.py", line 686 in repr_args
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/_code/code.py", line 776 in repr_traceback_entry
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/_code/code.py", line 825 in repr_traceback
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/_code/code.py", line 884 in repr_excinfo
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/_code/code.py", line 627 in getrepr
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/nodes.py", line 409 in _repr_failure_py
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/python.py", line 1663 in repr_failure
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/reports.py", line 318 in from_item_and_call
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/runner.py", line 336 in pytest_runtest_makereport
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/pluggy/callers.py", line 187 in _multicall
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/pluggy/manager.py", line 84 in <lambda>
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/pluggy/manager.py", line 93 in _hookexec
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/pluggy/hooks.py", line 286 in __call__
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/runner.py", line 218 in call_and_report
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/runner.py", line 127 in runtestprotocol
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/runner.py", line 110 in pytest_runtest_protocol
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/pluggy/callers.py", line 187 in _multicall
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/pluggy/manager.py", line 84 in <lambda>
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/pluggy/manager.py", line 93 in _hookexec
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/pluggy/hooks.py", line 286 in __call__
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/main.py", line 338 in pytest_runtestloop
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/pluggy/callers.py", line 187 in _multicall
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/pluggy/manager.py", line 84 in <lambda>
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/pluggy/manager.py", line 93 in _hookexec
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/pluggy/hooks.py", line 286 in __call__
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/main.py", line 313 in _main
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/main.py", line 257 in wrap_session
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/main.py", line 306 in pytest_cmdline_main
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/pluggy/callers.py", line 187 in _multicall
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/pluggy/manager.py", line 84 in <lambda>
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/pluggy/manager.py", line 93 in _hookexec
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/pluggy/hooks.py", line 286 in __call__
  File "/home/pbell/.conda/envs/pytorch-dev/lib/python3.8/site-packages/_pytest/config/__init__.py", line 164 in main
  File "/home/pbell/.conda/envs/pytorch-dev/bin/pytest", line 11 in <module>
Segmentation fault (core dumped)