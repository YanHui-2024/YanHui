(gdb) thread apply all bt

Thread 14 (Thread 0x7f7876ffd700 (LWP 12731)):
#0  futex_wait (val=785864, addr=0x5563f8bf1be4)
    at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/x86/futex.h:44
#1  do_wait (addr=addr@entry=0x5563f8bf1be4, val=val@entry=785864)
    at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/wait.h:67
#2  0x00007f794dfb7623 in gomp_barrier_wait_end (bar=0x5563f8bf1be0, state=785864)
    at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/bar.c:48
#3  0x00007f794dfb56f7 in gomp_simple_barrier_wait (bar=0x5563f8bf1be0)
    at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/posix/simple-bar.h:60
#4  gomp_thread_start (xdata=<optimized out>)
    at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/team.c:127
#5  0x00007f794ff7a6ba in start_thread (arg=0x7f7876ffd700) at pthread_create.c:333
#6  0x00007f794fcb041d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 13 (Thread 0x7f78777fe700 (LWP 12730)):
#0  futex_wait (val=785864, addr=0x5563f8bf1be4)
    at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/x86/futex.h:44
#1  do_wait (addr=addr@entry=0x5563f8bf1be4, val=val@entry=785864)
    at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/wait.h:67
#2  0x00007f794dfb7623 in gomp_barrier_wait_end (bar=0x5563f8bf1be0, state=785864)
    at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/bar.c:48
#3  0x00007f794dfb56f7 in gomp_simple_barrier_wait (bar=0x5563f8bf1be0)
    at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/posix/simple-bar.h:60
#4  gomp_thread_start (xdata=<optimized out>)
    at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/team.c:127
#5  0x00007f794ff7a6ba in start_thread (arg=0x7f78777fe700) at pthread_create.c:333
--Type <RET> for more, q to quit, c to continue without paging--c
#6  0x00007f794fcb041d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 12 (Thread 0x7f787c8c7700 (LWP 12729)):
#0  futex_wait (val=785864, addr=0x5563f8bf1be4) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/x86/futex.h:44
#1  do_wait (addr=addr@entry=0x5563f8bf1be4, val=val@entry=785864) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/wait.h:67
#2  0x00007f794dfb7623 in gomp_barrier_wait_end (bar=0x5563f8bf1be0, state=785864) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/bar.c:48
#3  0x00007f794dfb56f7 in gomp_simple_barrier_wait (bar=0x5563f8bf1be0) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/posix/simple-bar.h:60
#4  gomp_thread_start (xdata=<optimized out>) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/team.c:127
#5  0x00007f794ff7a6ba in start_thread (arg=0x7f787c8c7700) at pthread_create.c:333
#6  0x00007f794fcb041d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 11 (Thread 0x7f7877fff700 (LWP 12728)):
#0  futex_wait (val=785864, addr=0x5563f8bf1be4) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/x86/futex.h:44
#1  do_wait (addr=addr@entry=0x5563f8bf1be4, val=val@entry=785864) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/wait.h:67
#2  0x00007f794dfb7623 in gomp_barrier_wait_end (bar=0x5563f8bf1be0, state=785864) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/bar.c:48
#3  0x00007f794dfb56f7 in gomp_simple_barrier_wait (bar=0x5563f8bf1be0) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/posix/simple-bar.h:60
#4  gomp_thread_start (xdata=<optimized out>) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/team.c:127
#5  0x00007f794ff7a6ba in start_thread (arg=0x7f7877fff700) at pthread_create.c:333
#6  0x00007f794fcb041d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 10 (Thread 0x7f78ca946700 (LWP 12715)):
#0  futex_wait (val=785864, addr=0x5563f8bf1be4) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/x86/futex.h:44
#1  do_wait (addr=addr@entry=0x5563f8bf1be4, val=val@entry=785864) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/wait.h:67
#2  0x00007f794dfb7623 in gomp_barrier_wait_end (bar=0x5563f8bf1be0, state=785864) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/bar.c:48
#3  0x00007f794dfb56f7 in gomp_simple_barrier_wait (bar=0x5563f8bf1be0) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/posix/simple-bar.h:60
#4  gomp_thread_start (xdata=<optimized out>) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/team.c:127
#5  0x00007f794ff7a6ba in start_thread (arg=0x7f78ca946700) at pthread_create.c:333
#6  0x00007f794fcb041d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 9 (Thread 0x7f78cb147700 (LWP 12714)):
#0  futex_wait (val=785864, addr=0x5563f8bf1be4) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/x86/futex.h:44
#1  do_wait (addr=addr@entry=0x5563f8bf1be4, val=val@entry=785864) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/wait.h:67
#2  0x00007f794dfb7623 in gomp_barrier_wait_end (bar=0x5563f8bf1be0, state=785864) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/bar.c:48
#3  0x00007f794dfb56f7 in gomp_simple_barrier_wait (bar=0x5563f8bf1be0) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/posix/simple-bar.h:60
#4  gomp_thread_start (xdata=<optimized out>) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/team.c:127
#5  0x00007f794ff7a6ba in start_thread (arg=0x7f78cb147700) at pthread_create.c:333
#6  0x00007f794fcb041d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 8 (Thread 0x7f78727f4700 (LWP 1969)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00007f794def14cb in __gthread_cond_wait (__mutex=<optimized out>, __cond=<optimized out>) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/build/build-cc-gcc-final/x86_64-conda_cos6-linux-gnu/libstdc++-v3/include/x86_64-conda_cos6-linux-gnu/bits/gthr-default.h:878
#2  std::condition_variable::wait (this=<optimized out>, __lock=...) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libstdc++-v3/src/c++11/condition_variable.cc:53
#3  0x00007f7913cada93 in torch::autograd::ReadyQueue::pop() () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so
#4  0x00007f7913cb3e43 in torch::autograd::Engine::thread_main(std::shared_ptr<torch::autograd::GraphTask> const&, bool) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so
#5  0x00007f7913ca9810 in torch::autograd::Engine::thread_init(int, std::shared_ptr<torch::autograd::ReadyQueue> const&) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so
#6  0x00007f79195c5f00 in torch::autograd::python::PythonEngine::thread_init(int, std::shared_ptr<torch::autograd::ReadyQueue> const&) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_python.so
#7  0x00007f794def519d in std::execute_native_thread_routine (__p=0x5564073e2740) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libstdc++-v3/src/c++11/thread.cc:80
#8  0x00007f794ff7a6ba in start_thread (arg=0x7f78727f4700) at pthread_create.c:333
#9  0x00007f794fcb041d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 7 (Thread 0x7f7872ff5700 (LWP 1968)):
#0  pthread_cond_wait@@GLIBC_2.3.2 () at ../sysdeps/unix/sysv/linux/x86_64/pthread_cond_wait.S:185
#1  0x00007f794def14cb in __gthread_cond_wait (__mutex=<optimized out>, __cond=<optimized out>) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/build/build-cc-gcc-final/x86_64-conda_cos6-linux-gnu/libstdc++-v3/include/x86_64-conda_cos6-linux-gnu/bits/gthr-default.h:878
#2  std::condition_variable::wait (this=<optimized out>, __lock=...) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libstdc++-v3/src/c++11/condition_variable.cc:53
#3  0x00007f7913cada93 in torch::autograd::ReadyQueue::pop() () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so
#4  0x00007f7913cb3e43 in torch::autograd::Engine::thread_main(std::shared_ptr<torch::autograd::GraphTask> const&, bool) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so
#5  0x00007f7913ca9810 in torch::autograd::Engine::thread_init(int, std::shared_ptr<torch::autograd::ReadyQueue> const&) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so
#6  0x00007f79195c5f00 in torch::autograd::python::PythonEngine::thread_init(int, std::shared_ptr<torch::autograd::ReadyQueue> const&) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_python.so
#7  0x00007f794def519d in std::execute_native_thread_routine (__p=0x55640a7db640) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libstdc++-v3/src/c++11/thread.cc:80
#8  0x00007f794ff7a6ba in start_thread (arg=0x7f7872ff5700) at pthread_create.c:333
#9  0x00007f794fcb041d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 6 (Thread 0x7f78737f6700 (LWP 1712)):
#0  0x00007f794fcb18c8 in accept4 (fd=37, addr=..., addr_len=0x7f78737f4f34, flags=524288) at ../sysdeps/unix/sysv/linux/accept4.c:40
#1  0x00007f78f5d19a5b in sock_accept_impl (data=<synthetic pointer>, s=<optimized out>) at /usr/local/src/conda/python-3.6.10/Modules/socketmodule.c:2388
#2  sock_call_ex (timeout=-1000000000, err=0x0, connect=0, data=<synthetic pointer>, sock_func=<optimized out>, writing=0, s=0x7f78d2682048) at /usr/local/src/conda/python-3.6.10/Modules/socketmodule.c:900
#3  sock_call () at /usr/local/src/conda/python-3.6.10/Modules/socketmodule.c:952
#4  sock_accept (s=0x7f78d2682048) at /usr/local/src/conda/python-3.6.10/Modules/socketmodule.c:2430
#5  0x00005563c042057a in _PyCFunction_FastCallDict (func_obj=0x7f78d2677cf0, args=0x7f78d2cff7c0, nargs=0, kwargs=0x0) at /tmp/build/80754af9/python_1585002248360/work/Objects/methodobject.c:192
#6  0x00005563c04a7aac in call_function (pp_stack=0x7f78737f5178, oparg=<optimized out>, kwnames=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4851
#7  0x00005563c04ca19a in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3335
#8  0x00005563c04a1c6b in _PyFunction_FastCall (globals=<optimized out>, nargs=1, args=<optimized out>, co=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4933
#9  fast_function (func=<optimized out>, stack=0x7f78d2683388, nargs=1, kwnames=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4968
#10 0x00005563c04a7b85 in call_function (pp_stack=0x7f78737f5328, oparg=<optimized out>, kwnames=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4872
#11 0x00005563c04ca19a in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3335
#12 0x00005563c04a1c6b in _PyFunction_FastCall (globals=<optimized out>, nargs=1, args=<optimized out>, co=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4933
#13 fast_function (func=<optimized out>, stack=0x7f78d20c68d0, nargs=1, kwnames=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4968
#14 0x00005563c04a7b85 in call_function (pp_stack=0x7f78737f54d8, oparg=<optimized out>, kwnames=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4872
#15 0x00005563c04ca19a in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3335
#16 0x00005563c04a1c6b in _PyFunction_FastCall (globals=<optimized out>, nargs=1, args=<optimized out>, co=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4933
#17 fast_function (func=<optimized out>, stack=0x7f783c001028, nargs=1, kwnames=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4968
#18 0x00005563c04a7b85 in call_function (pp_stack=0x7f78737f5688, oparg=<optimized out>, kwnames=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4872
#19 0x00005563c04ca19a in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3335
#20 0x00005563c04a22db in _PyFunction_FastCall (globals=<optimized out>, nargs=1, args=<optimized out>, co=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4933
#21 _PyFunction_FastCallDict (func=<optimized out>, args=0x7f78737f5810, nargs=1, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5035
#22 0x00005563c04208ff in _PyObject_FastCallDict (func=0x7f78f5d4a6a8, args=0x7f78737f5810, nargs=<optimized out>, kwargs=0x7f78d2687c60) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2310
#23 0x00005563c0425363 in _PyObject_Call_Prepend (func=0x7f78f5d4a6a8, obj=<optimized out>, args=0x7f7950363048, kwargs=0x7f78d2687c60) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2373
#24 0x00005563c042033e in PyObject_Call (func=0x7f78d233ac88, args=<optimized out>, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2261
#25 0x00005563c04cb7fd in do_call_core (kwdict=0x7f78d2687c60, callargs=0x7f7950363048, func=0x7f78d233ac88) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5120
#26 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3404
#27 0x00005563c04a1c6b in _PyFunction_FastCall (globals=<optimized out>, nargs=1, args=<optimized out>, co=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4933
#28 fast_function (func=<optimized out>, stack=0x7f783c000a70, nargs=1, kwnames=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4968
#29 0x00005563c04a7b85 in call_function (pp_stack=0x7f78737f5b08, oparg=<optimized out>, kwnames=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4872
#30 0x00005563c04ca19a in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3335
#31 0x00005563c04a1c6b in _PyFunction_FastCall (globals=<optimized out>, nargs=1, args=<optimized out>, co=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4933
#32 fast_function (func=<optimized out>, stack=0x7f78d265b968, nargs=1, kwnames=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4968
#33 0x00005563c04a7b85 in call_function (pp_stack=0x7f78737f5cb8, oparg=<optimized out>, kwnames=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4872
#34 0x00005563c04ca19a in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3335
#35 0x00005563c04a22db in _PyFunction_FastCall (globals=<optimized out>, nargs=1, args=<optimized out>, co=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4933
#36 _PyFunction_FastCallDict (func=<optimized out>, args=0x7f78737f5e40, nargs=1, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5035
#37 0x00005563c04208ff in _PyObject_FastCallDict (func=0x7f794dd79ae8, args=0x7f78737f5e40, nargs=<optimized out>, kwargs=0x0) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2310
#38 0x00005563c0425363 in _PyObject_Call_Prepend (func=0x7f794dd79ae8, obj=<optimized out>, args=0x7f7950363048, kwargs=0x0) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2373
#39 0x00005563c042033e in PyObject_Call (func=0x7f78d233af48, args=<optimized out>, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2261
#40 0x00005563c051d8f6 in t_bootstrap (boot_raw=boot_raw@entry=0x7f78d2d4daf8) at /tmp/build/80754af9/python_1585002248360/work/Modules/_threadmodule.c:1000
#41 0x00005563c04d10c8 in pythread_wrapper (arg=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/thread_pthread.h:205
#42 0x00007f794ff7a6ba in start_thread (arg=0x7f78737f6700) at pthread_create.c:333
#43 0x00007f794fcb041d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 5 (Thread 0x7f78c9fe3700 (LWP 1409)):
#0  futex_wait (val=785864, addr=0x5563f8bf1be4) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/x86/futex.h:44
#1  do_wait (addr=addr@entry=0x5563f8bf1be4, val=val@entry=785864) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/wait.h:67
#2  0x00007f794dfb7623 in gomp_barrier_wait_end (bar=0x5563f8bf1be0, state=785864) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/linux/bar.c:48
#3  0x00007f794dfb56f7 in gomp_simple_barrier_wait (bar=0x5563f8bf1be0) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/config/posix/simple-bar.h:60
#4  gomp_thread_start (xdata=<optimized out>) at /home/nwani/m3/conda-bld/compilers_linux-64_1560109574129/work/.build/x86_64-conda_cos6-linux-gnu/src/gcc/libgomp/team.c:127
#5  0x00007f794ff7a6ba in start_thread (arg=0x7f78c9fe3700) at pthread_create.c:333
#6  0x00007f794fcb041d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 4 (Thread 0x7f78c97e2700 (LWP 1408)):
#0  0x00007f794fca474d in poll () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007f78f42ff793 in ?? () from /usr/lib/x86_64-linux-gnu/libcuda.so.1
#2  0x00007f78f43a19ca in ?? () from /usr/lib/x86_64-linux-gnu/libcuda.so.1
#3  0x00007f78f4301e18 in ?? () from /usr/lib/x86_64-linux-gnu/libcuda.so.1
#4  0x00007f794ff7a6ba in start_thread (arg=0x7f78c97e2700) at pthread_create.c:333
#5  0x00007f794fcb041d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 3 (Thread 0x7f78c8fe1700 (LWP 1407)):
#0  0x00007f794fca474d in poll () at ../sysdeps/unix/syscall-template.S:84
#1  0x00007f78f42ff793 in ?? () from /usr/lib/x86_64-linux-gnu/libcuda.so.1
#2  0x00007f78f43a19ca in ?? () from /usr/lib/x86_64-linux-gnu/libcuda.so.1
#3  0x00007f78f4301e18 in ?? () from /usr/lib/x86_64-linux-gnu/libcuda.so.1
#4  0x00007f794ff7a6ba in start_thread (arg=0x7f78c8fe1700) at pthread_create.c:333
#5  0x00007f794fcb041d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 2 (Thread 0x7f78f40d5700 (LWP 1373)):
#0  0x00007f794fcb18c8 in accept4 (fd=12, addr=..., addr_len=0x7f78f40d4e58, flags=524288) at ../sysdeps/unix/sysv/linux/accept4.c:40
#1  0x00007f78f430075a in ?? () from /usr/lib/x86_64-linux-gnu/libcuda.so.1
#2  0x00007f78f42f22bd in ?? () from /usr/lib/x86_64-linux-gnu/libcuda.so.1
#3  0x00007f78f4301e18 in ?? () from /usr/lib/x86_64-linux-gnu/libcuda.so.1
#4  0x00007f794ff7a6ba in start_thread (arg=0x7f78f40d5700) at pthread_create.c:333
#5  0x00007f794fcb041d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 1 (Thread 0x7f79503a4700 (LWP 1369)):
#0  __GI___libc_free (mem=0x5564600851d0) at malloc.c:2934
#1  0x00007f7913e3d920 in torch::jit::LivenessAnalyzer::processBlock(torch::jit::Block*, c10::SparseBitVector<256u>) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so
#2  0x00007f7913e3e574 in torch::jit::LivenessAnalyzer::processBlock(torch::jit::Block*, c10::SparseBitVector<256u>) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so
#3  0x00007f7913e3e574 in torch::jit::LivenessAnalyzer::processBlock(torch::jit::Block*, c10::SparseBitVector<256u>) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so
#4  0x00007f7913e3c851 in torch::jit::BuildLivenessSets(std::shared_ptr<torch::jit::Graph>) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so
#5  0x00007f7913dc1108 in torch::jit::InsertBailOuts(std::shared_ptr<torch::jit::Graph>) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so
#6  0x00007f7913da7dff in torch::jit::ProfilingGraphExecutorImpl::runProfilingOptimizations(std::shared_ptr<torch::jit::Graph>&) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so
#7  0x00007f7913da8cbf in torch::jit::ProfilingGraphExecutorImpl::getPlanFor(std::vector<c10::IValue, std::allocator<c10::IValue> >&, unsigned long) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so
#8  0x00007f7913d1db65 in torch::jit::GraphExecutorImplBase::run(std::vector<c10::IValue, std::allocator<c10::IValue> >&) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so
#9  0x00007f791968279c in torch::jit::runAndInsertCall(torch::jit::Function&, torch::jit::tuple_slice, pybind11::kwargs, c10::optional<c10::IValue>, std::function<torch::jit::Value* (torch::jit::Graph&, torch::jit::MatchedSchema const&)>) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_python.so
#10 0x00007f79197331bc in torch::jit::invokeScriptFunctionFromPython(torch::jit::Function&, torch::jit::tuple_slice, pybind11::kwargs) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_python.so
#11 0x00007f79196fa848 in torch::jit::initJitScriptBindings(_object*)::{lambda(pybind11::args, pybind11::kwargs)#23}::operator()(pybind11::args, pybind11::kwargs) const [clone .isra.3432] () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_python.so
#12 0x00007f79196fb025 in pybind11::cpp_function::initialize<torch::jit::initJitScriptBindings(_object*)::{lambda(pybind11::args, pybind11::kwargs)#23}, pybind11::object, pybind11::args, pybind11::kwargs, pybind11::name, pybind11::is_method, pybind11::sibling>(torch::jit::initJitScriptBindings(_object*)::{lambda(pybind11::args, pybind11::kwargs)#23}&&, pybind11::object (*)(pybind11::args, pybind11::kwargs), pybind11::name const&, pybind11::is_method const&, pybind11::sibling const&)::{lambda(pybind11::detail::function_call&)#3}::_FUN(pybind11::detail::function_call) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_python.so
#13 0x00007f79192ebde8 in pybind11::cpp_function::dispatcher(_object*, _object*, _object*) () from /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_python.so
#14 0x00005563c0423476 in PyCFunction_Call (func=0x7f794d2fe438, args=<optimized out>, kwds=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/methodobject.c:98
#15 0x00005563c042033e in PyObject_Call (func=0x7f794d2fe438, args=<optimized out>, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2261
#16 0x00005563c042033e in PyObject_Call (func=0x7f794d2fceb8, args=<optimized out>, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2261
#17 0x00005563c04cb7fd in do_call_core (kwdict=0x7f78d23db3f0, callargs=0x7f78d2d108c8, func=0x7f794d2fceb8) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5120
#18 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3404
#19 0x00005563c04a29b9 in _PyEval_EvalCodeWithName (qualname=0x0, name=<optimized out>, closure=0x0, kwdefs=0x0, defcount=0, defs=0x0, kwstep=2, kwcount=<optimized out>, kwargs=0x7f78d23ed428, kwnames=0x7f78d23ed420, argcount=<optimized out>, args=<optimized out>, locals=<optimized out>, globals=<optimized out>, _co=0x7f78f57cb390) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4166
#20 PyEval_EvalCodeEx (_co=0x7f78f57cb390, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kws=0x7f78d23ed420, kwcount=1, defs=0x0, defcount=0, kwdefs=0x0, closure=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4187
#21 0x00005563c04a38d6 in function_call (func=func@entry=0x7f78f5773950, arg=0x7f78d23f3fc0, kw=0x7f78d23db558) at /tmp/build/80754af9/python_1585002248360/work/Objects/funcobject.c:604
#22 0x00005563c042033e in PyObject_Call (func=0x7f78f5773950, args=<optimized out>, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2261
#23 0x00005563c04cb7fd in do_call_core (kwdict=0x7f78d23db558, callargs=0x7f78d23f3fc0, func=0x7f78f5773950) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5120
#24 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3404
#25 0x00005563c04a0ff4 in _PyEval_EvalCodeWithName (_co=0x7f78f57cb420, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=0x7f78d2d10a20, kwargs=0x7f78d2d10a28, kwcount=<optimized out>, kwstep=2, defs=0x0, defcount=0, kwdefs=0x0, closure=0x0, name=<optimized out>, qualname=0x7f78f57ca570) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4166
#26 0x00005563c04a259a in _PyFunction_FastCallDict (func=<optimized out>, args=0x7ffc3abb5c10, nargs=2, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5084
#27 0x00005563c04208ff in _PyObject_FastCallDict (func=0x7f78f57739d8, args=0x7ffc3abb5c10, nargs=<optimized out>, kwargs=0x7f78d23db990) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2310
#28 0x00005563c0425363 in _PyObject_Call_Prepend (func=0x7f78f57739d8, obj=<optimized out>, args=0x7f78d2438cf8, kwargs=0x7f78d23db990) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2373
#29 0x00005563c042033e in PyObject_Call (func=0x7f78d24524c8, args=<optimized out>, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2261
#30 0x00005563c0479121 in slot_tp_call (self=self@entry=0x7f78d26a5518, args=0x7f78d2438cf8, kwds=0x7f78d23db990) at /tmp/build/80754af9/python_1585002248360/work/Objects/typeobject.c:6207
#31 0x00005563c042033e in PyObject_Call (func=0x7f78d26a5518, args=<optimized out>, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2261
#32 0x00005563c04cb7fd in do_call_core (kwdict=0x7f78d23db990, callargs=0x7f78d2438cf8, func=0x7f78d26a5518) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5120
#33 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3404
#34 0x00005563c04a1333 in _PyEval_EvalCodeWithName (_co=0x7f794f1c7300, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=0x0, kwargs=0x55640c5163f0, kwcount=<optimized out>, kwstep=1, defs=0x0, defcount=0, kwdefs=0x0, closure=0x7f78d25b5828, name=<optimized out>, qualname=0x7f794f1c0ab0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4166
#35 0x00005563c04a1ea1 in fast_function (func=<optimized out>, stack=0x55640c5163c8, nargs=5, kwnames=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4992
#36 0x00005563c04a7b85 in call_function (pp_stack=0x7ffc3abb6088, oparg=<optimized out>, kwnames=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4872
#37 0x00005563c04ca19a in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3335
#38 0x00005563c04a2ff6 in _PyEval_EvalCodeWithName (qualname=0x0, name=<optimized out>, closure=0x0, kwdefs=0x0, defcount=0, defs=0x0, kwstep=2, kwcount=<optimized out>, kwargs=0x7f7950363068, kwnames=0x7f7950363060, argcount=<optimized out>, args=<optimized out>, locals=<optimized out>, globals=<optimized out>, _co=0x7f794f1c7390) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4166
#39 PyEval_EvalCodeEx (_co=0x7f794f1c7390, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kws=0x7f7950363060, kwcount=0, defs=0x0, defcount=0, kwdefs=0x0, closure=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4187
#40 0x00005563c04a38d6 in function_call (func=func@entry=0x7f78d542a378, arg=0x7f78d23f6108, kw=0x7f78d23db678) at /tmp/build/80754af9/python_1585002248360/work/Objects/funcobject.c:604
#41 0x00005563c042033e in PyObject_Call (func=0x7f78d542a378, args=<optimized out>, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2261
#42 0x00005563c04cb7fd in do_call_core (kwdict=0x7f78d23db678, callargs=0x7f78d23f6108, func=0x7f78d542a378) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5120
#43 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3404
#44 0x00005563c04a2ff6 in _PyEval_EvalCodeWithName (qualname=0x0, name=<optimized out>, closure=0x7f78d5409d48, kwdefs=0x0, defcount=0, defs=0x0, kwstep=2, kwcount=<optimized out>, kwargs=0x7f7950363068, kwnames=0x7f7950363060, argcount=<optimized out>, args=<optimized out>, locals=<optimized out>, globals=<optimized out>, _co=0x7f78f57c0780) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4166
#45 PyEval_EvalCodeEx (_co=0x7f78f57c0780, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kws=0x7f7950363060, kwcount=0, defs=0x0, defcount=0, kwdefs=0x0, closure=0x7f78d5409d48) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4187
#46 0x00005563c04a38d6 in function_call (func=func@entry=0x7f78d542a400, arg=0x7f78d23f6908, kw=0x7f78d23dbf30) at /tmp/build/80754af9/python_1585002248360/work/Objects/funcobject.c:604
#47 0x00005563c042033e in PyObject_Call (func=0x7f78d542a400, args=<optimized out>, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2261
#48 0x00005563c04cb7fd in do_call_core (kwdict=0x7f78d23dbf30, callargs=0x7f78d23f6908, func=0x7f78d542a400) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5120
#49 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3404
#50 0x00005563c04a1333 in _PyEval_EvalCodeWithName (_co=0x7f78f57c0780, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=0x0, kwargs=0x7f78d23535c8, kwcount=<optimized out>, kwstep=1, defs=0x0, defcount=0, kwdefs=0x0, closure=0x7f78d5409d88, name=<optimized out>, qualname=0x7f794f1bd8c8) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4166
#51 0x00005563c04a1ea1 in fast_function (func=<optimized out>, stack=0x7f78d23535b8, nargs=2, kwnames=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4992
#52 0x00005563c04a7b85 in call_function (pp_stack=0x7ffc3abb68c8, oparg=<optimized out>, kwnames=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4872
#53 0x00005563c04ca19a in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3335
#54 0x00005563c04a1196 in _PyEval_EvalCodeWithName (_co=0x7f78f57aeed0, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=0x7f7950363060, kwargs=0x7f7950363068, kwcount=<optimized out>, kwstep=2, defs=0x7f78d5218450, defcount=1, kwdefs=0x0, closure=0x7f78d52184e0, name=<optimized out>, qualname=0x7f794f1bd8c8) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4166
#55 0x00005563c04a259a in _PyFunction_FastCallDict (func=<optimized out>, args=0x7ffc3abb6b80, nargs=1, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5084
#56 0x00005563c04208ff in _PyObject_FastCallDict (func=0x7f78d5216d90, args=0x7ffc3abb6b80, nargs=<optimized out>, kwargs=0x7f78d23dbab0) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2310
#57 0x00005563c0425363 in _PyObject_Call_Prepend (func=0x7f78d5216d90, obj=<optimized out>, args=0x7f7950363048, kwargs=0x7f78d23dbab0) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2373
#58 0x00005563c042033e in PyObject_Call (func=0x7f78d23fa848, args=<optimized out>, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2261
#59 0x00005563c04cb7fd in do_call_core (kwdict=0x7f78d23dbab0, callargs=0x7f7950363048, func=0x7f78d23fa848) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5120
#60 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3404
#61 0x00005563c04a1333 in _PyEval_EvalCodeWithName (_co=0x7f78f57d34b0, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=0x0, kwargs=0x5563ecba2528, kwcount=<optimized out>, kwstep=1, defs=0x0, defcount=0, kwdefs=0x0, closure=0x7f78d23fa7c8, name=<optimized out>, qualname=0x7f794f1bd8c8) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4166
#62 0x00005563c04a1ea1 in fast_function (func=<optimized out>, stack=0x5563ecba2520, nargs=1, kwnames=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4992
#63 0x00005563c04a7b85 in call_function (pp_stack=0x7ffc3abb6fa8, oparg=<optimized out>, kwnames=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4872
#64 0x00005563c04ca19a in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3335
#65 0x00005563c04a0ff4 in _PyEval_EvalCodeWithName (_co=0x7f78fa187c90, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=0x7f7950363060, kwargs=0x7f7950363068, kwcount=<optimized out>, kwstep=2, defs=0x7f78fa191760, defcount=1, kwdefs=0x0, closure=0x0, name=<optimized out>, qualname=0x7f78fa1848f0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4166
#66 0x00005563c04a259a in _PyFunction_FastCallDict (func=<optimized out>, args=0x7ffc3abb7260, nargs=2, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5084
#67 0x00005563c04208ff in _PyObject_FastCallDict (func=0x7f78fa16a1e0, args=0x7ffc3abb7260, nargs=<optimized out>, kwargs=0x7f78d25c4678) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2310
#68 0x00005563c0425363 in _PyObject_Call_Prepend (func=0x7f78fa16a1e0, obj=<optimized out>, args=0x7f78d2cf5080, kwargs=0x7f78d25c4678) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2373
#69 0x00005563c042033e in PyObject_Call (func=0x7f78d2329e88, args=<optimized out>, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2261
#70 0x00005563c04cb7fd in do_call_core (kwdict=0x7f78d25c4678, callargs=0x7f78d2cf5080, func=0x7f78d2329e88) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5120
#71 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3404
#72 0x00005563c04a0ff4 in _PyEval_EvalCodeWithName (_co=0x7f78fa187db0, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=0x0, kwargs=0x0, kwcount=<optimized out>, kwstep=2, defs=0x0, defcount=0, kwdefs=0x0, closure=0x0, name=<optimized out>, qualname=0x7f78fa186978) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4166
#73 0x00005563c04a237c in _PyFunction_FastCallDict (func=<optimized out>, args=0x7ffc3abb7660, nargs=2, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5084
#74 0x00005563c04208ff in _PyObject_FastCallDict (func=0x7f78fa16a2f0, args=0x7ffc3abb7660, nargs=<optimized out>, kwargs=0x0) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2310
#75 0x00005563c0425363 in _PyObject_Call_Prepend (func=0x7f78fa16a2f0, obj=<optimized out>, args=0x7f78d2f79320, kwargs=0x0) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2373
#76 0x00005563c042033e in PyObject_Call (func=0x7f7950355ac8, args=<optimized out>, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2261
#77 0x00005563c0479121 in slot_tp_call (self=self@entry=0x7f78d23e1b70, args=args@entry=0x7f78d2f79320, kwds=kwds@entry=0x0) at /tmp/build/80754af9/python_1585002248360/work/Objects/typeobject.c:6207
#78 0x00005563c042071b in _PyObject_FastCallDict (func=0x7f78d23e1b70, args=0x7f78d2dfada0, nargs=<optimized out>, kwargs=0x0) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2331
#79 0x00005563c04a7bfe in call_function (pp_stack=0x7ffc3abb7868, oparg=<optimized out>, kwnames=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4875
#80 0x00005563c04ca19a in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3335
#81 0x00005563c04a0ff4 in _PyEval_EvalCodeWithName (_co=0x7f78fa19c4b0, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=0x7f7950363060, kwargs=0x7f7950363068, kwcount=<optimized out>, kwstep=2, defs=0x7f78fa169680, defcount=1, kwdefs=0x0, closure=0x0, name=<optimized out>, qualname=0x7f78fa165930) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4166
#82 0x00005563c04a259a in _PyFunction_FastCallDict (func=<optimized out>, args=0x7ffc3abb7b20, nargs=2, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5084
#83 0x00005563c04208ff in _PyObject_FastCallDict (func=0x7f78fa16cea0, args=0x7ffc3abb7b20, nargs=<optimized out>, kwargs=0x7f78d2f8f480) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2310
#84 0x00005563c0425363 in _PyObject_Call_Prepend (func=0x7f78fa16cea0, obj=<optimized out>, args=0x7f78d2f79390, kwargs=0x7f78d2f8f480) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2373
#85 0x00005563c042033e in PyObject_Call (func=0x7f794d234148, args=<optimized out>, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2261
#86 0x00005563c04cb7fd in do_call_core (kwdict=0x7f78d2f8f480, callargs=0x7f78d2f79390, func=0x7f794d234148) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5120
#87 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3404
#88 0x00005563c04a0ff4 in _PyEval_EvalCodeWithName (_co=0x7f78fa1949c0, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=0x0, kwargs=0x0, kwcount=<optimized out>, kwstep=2, defs=0x0, defcount=0, kwdefs=0x0, closure=0x0, name=<optimized out>, qualname=0x7f78fa178db0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4166
#89 0x00005563c04a237c in _PyFunction_FastCallDict (func=<optimized out>, args=0x7ffc3abb7f20, nargs=2, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5084
#90 0x00005563c04208ff in _PyObject_FastCallDict (func=0x7f78fa16cd90, args=0x7ffc3abb7f20, nargs=<optimized out>, kwargs=0x0) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2310
#91 0x00005563c0425363 in _PyObject_Call_Prepend (func=0x7f78fa16cd90, obj=<optimized out>, args=0x7f78d2f792e8, kwargs=0x0) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2373
#92 0x00005563c042033e in PyObject_Call (func=0x7f78f5d5bf48, args=<optimized out>, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2261
#93 0x00005563c0479121 in slot_tp_call (self=self@entry=0x7f78d2f79b00, args=args@entry=0x7f78d2f792e8, kwds=kwds@entry=0x0) at /tmp/build/80754af9/python_1585002248360/work/Objects/typeobject.c:6207
#94 0x00005563c042071b in _PyObject_FastCallDict (func=0x7f78d2f79b00, args=0x5563c584c560, nargs=<optimized out>, kwargs=0x0) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2331
#95 0x00005563c04a7bfe in call_function (pp_stack=0x7ffc3abb8128, oparg=<optimized out>, kwnames=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4875
#96 0x00005563c04ca19a in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3335
#97 0x00005563c04a1c6b in _PyFunction_FastCall (globals=<optimized out>, nargs=2, args=<optimized out>, co=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4933
#98 fast_function (func=<optimized out>, stack=0x5563ecb6d5d0, nargs=2, kwnames=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4968
#99 0x00005563c04a7b85 in call_function (pp_stack=0x7ffc3abb82d8, oparg=<optimized out>, kwnames=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4872
#100 0x00005563c04ca19a in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3335
#101 0x00005563c04a1c6b in _PyFunction_FastCall (globals=<optimized out>, nargs=1, args=<optimized out>, co=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4933
#102 fast_function (func=<optimized out>, stack=0x5563c53f5c60, nargs=1, kwnames=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4968
#103 0x00005563c04a7b85 in call_function (pp_stack=0x7ffc3abb8488, oparg=<optimized out>, kwnames=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4872
#104 0x00005563c04ca19a in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3335
#105 0x00005563c04a147b in _PyEval_EvalCodeWithName (_co=0x7f78fa0fd150, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=0x7f78d53861a0, kwargs=0x7f78d53861a8, kwcount=<optimized out>, kwstep=2, defs=0x7f78fa0dc390, defcount=11, kwdefs=0x7f78fa17ca68, closure=0x0, name=<optimized out>, qualname=0x7f78fa17c4f8) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4166
#106 0x00005563c04a259a in _PyFunction_FastCallDict (func=<optimized out>, args=0x7ffc3abb8740, nargs=1, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:5084
#107 0x00005563c04208ff in _PyObject_FastCallDict (func=0x7f78fa0dc400, args=0x7ffc3abb8740, nargs=<optimized out>, kwargs=0x7f78d52c96c0) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2310
#108 0x00005563c0425363 in _PyObject_Call_Prepend (func=0x7f78fa0dc400, obj=<optimized out>, args=0x7f7950363048, kwargs=0x7f78d52c96c0) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2373
#109 0x00005563c042033e in PyObject_Call (func=0x7f794c56a348, args=<optimized out>, kwargs=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2261
#110 0x00005563c047879b in slot_tp_init (self=self@entry=0x7f78d2f793c8, args=args@entry=0x7f7950363048, kwds=kwds@entry=0x7f78d52c96c0) at /tmp/build/80754af9/python_1585002248360/work/Objects/typeobject.c:6420
#111 0x00005563c04a7de7 in type_call (type=<optimized out>, type@entry=0x5563c43fcd58, args=args@entry=0x7f7950363048, kwds=kwds@entry=0x7f78d52c96c0) at /tmp/build/80754af9/python_1585002248360/work/Objects/typeobject.c:915
#112 0x00005563c042071b in _PyObject_FastCallDict (func=0x5563c43fcd58, args=0x5563c57eb428, nargs=<optimized out>, kwargs=0x7f78d52c96c0) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2331
#113 0x00005563c04a218a in _PyObject_FastCallKeywords (func=0x5563c43fcd58, stack=0x5563c57eb428, nargs=0, kwnames=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Objects/abstract.c:2496
#114 0x00005563c04a7bfe in call_function (pp_stack=0x7ffc3abb89c0, oparg=<optimized out>, kwnames=0x7f78f57cac48) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4875
#115 0x00005563c04caf5a in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3351
#116 0x00005563c04a1333 in _PyEval_EvalCodeWithName (_co=0x7f78f57cb810, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=0x0, kwargs=0x5563c25830f8, kwcount=<optimized out>, kwstep=1, defs=0x7f78f5775b88, defcount=1, kwdefs=0x0, closure=0x0, name=<optimized out>, qualname=0x7f794dd766f0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4166
#117 0x00005563c04a1ea1 in fast_function (func=<optimized out>, stack=0x5563c25830f8, nargs=0, kwnames=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4992
#118 0x00005563c04a7b85 in call_function (pp_stack=0x7ffc3abb8c98, oparg=<optimized out>, kwnames=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4872
#119 0x00005563c04ca19a in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:3335
#120 0x00005563c04a29b9 in _PyEval_EvalCodeWithName (qualname=0x0, name=<optimized out>, closure=0x0, kwdefs=0x0, defcount=0, defs=0x0, kwstep=2, kwcount=<optimized out>, kwargs=0x0, kwnames=0x0, argcount=<optimized out>, args=<optimized out>, locals=<optimized out>, globals=<optimized out>, _co=0x7f794f0f28a0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4166
#121 PyEval_EvalCodeEx (_co=0x7f794f0f28a0, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kws=0x0, kwcount=0, defs=0x0, defcount=0, kwdefs=0x0, closure=0x0) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:4187
#122 0x00005563c04a374c in PyEval_EvalCode (co=co@entry=0x7f794f0f28a0, globals=globals@entry=0x7f795031a168, locals=locals@entry=0x7f795031a168) at /tmp/build/80754af9/python_1585002248360/work/Python/ceval.c:731
#123 0x00005563c0523634 in run_mod (mod=<optimized out>, filename=<optimized out>, globals=0x7f795031a168, locals=0x7f795031a168, flags=<optimized out>, arena=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Python/pythonrun.c:1025
#124 0x00005563c0523a31 in PyRun_FileExFlags (fp=0x5563c23fa590, filename_str=<optimized out>, start=<optimized out>, globals=0x7f795031a168, locals=0x7f795031a168, closeit=1, flags=0x7ffc3abb8f3c) at /tmp/build/80754af9/python_1585002248360/work/Python/pythonrun.c:978
#125 0x00005563c0523c33 in PyRun_SimpleFileExFlags (fp=0x5563c23fa590, filename=<optimized out>, closeit=1, flags=0x7ffc3abb8f3c) at /tmp/build/80754af9/python_1585002248360/work/Python/pythonrun.c:419
#126 0x00005563c0527723 in run_file (p_cf=0x7ffc3abb8f3c, filename=0x5563c23690f0 L"test_torch.py", fp=0x5563c23fa590) at /tmp/build/80754af9/python_1585002248360/work/Modules/main.c:340
#127 Py_Main (argc=<optimized out>, argv=<optimized out>) at /tmp/build/80754af9/python_1585002248360/work/Modules/main.c:811
#128 0x00005563c03f21fe in main (argc=3, argv=0x7ffc3abb9148) at /tmp/build/80754af9/python_1585002248360/work/Programs/python.c:69