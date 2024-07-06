(gdb) bt
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x00007ffff7c69859 in __GI_abort () at abort.c:79
#2  0x00007ffff7c69729 in __assert_fail_base (fmt=0x7ffff7dff588 "%s%s%s:%u: %s%sAssertion `%s' failed.\n%n", 
    assertion=0x55555576a56a "_PyGCHead_REFS(gc) != 0", file=0x55555576a520 "Modules/gcmodule.c", line=380, function=<optimized out>)
    at assert.c:92
#3  0x00007ffff7c7af36 in __GI___assert_fail (assertion=assertion@entry=0x55555576a56a "_PyGCHead_REFS(gc) != 0", 
    file=file@entry=0x55555576a520 "Modules/gcmodule.c", line=line@entry=380, 
    function=function@entry=0x55555576aac8 <__PRETTY_FUNCTION__.14474> "visit_decref") at assert.c:101
#4  0x00005555555c6900 in visit_decref (op=0x7fff84979bb8, data=<optimized out>) at Modules/gcmodule.c:384
#5  0x000055555561d480 in dict_traverse (op=<optimized out>, visit=0x5555555c6876 <visit_decref>, arg=0x0) at Objects/dictobject.c:3046
#6  0x00005555555c5ff9 in subtract_refs (containers=containers@entry=0x5555558162a0 <generations>) at Modules/gcmodule.c:399
#7  0x00005555555c7292 in collect (generation=generation@entry=0, n_collected=n_collected@entry=0x7fffffff9888, 
    n_uncollectable=n_uncollectable@entry=0x7fffffff9890, nofail=nofail@entry=0) at Modules/gcmodule.c:953
#8  0x00005555555c7787 in collect_with_callback (generation=0) at Modules/gcmodule.c:1128
#9  0x00005555555c78c4 in collect_generations () at Modules/gcmodule.c:1151
#10 0x00005555555c7a5f in _PyObject_GC_Alloc (use_calloc=use_calloc@entry=0, basicsize=<optimized out>) at Modules/gcmodule.c:1729
#11 0x00005555555c7fb0 in _PyObject_GC_Malloc (basicsize=<optimized out>) at Modules/gcmodule.c:1739
#12 0x00005555555c7fe5 in _PyObject_GC_New (tp=tp@entry=0x555555829a20 <PyFunction_Type>) at Modules/gcmodule.c:1751
#13 0x000055555560b03a in PyFunction_NewWithQualName (code=code@entry=0x7ffee3695ac0, globals=0x7ffee36ff8c8, 
    qualname=qualname@entry=0x7ffee3691670) at Objects/funcobject.c:21
#14 0x00005555556d4eb1 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3419
#15 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x5555578a7a58, throwflag=throwflag@entry=0) at Python/ceval.c:754
#16 0x00005555556c9ac6 in _PyEval_EvalCodeWithName (_co=0x7ffee3695b80, globals=<optimized out>, locals=locals@entry=0x0, 
    args=<optimized out>, argcount=2, kwnames=0x0, kwargs=0x55555859d7b8, kwcount=0, kwstep=1, defs=0x0, defcount=0, kwdefs=0x0, 
    closure=0x0, name=0x7ffee3699900, qualname=0x7ffee3698310) at Python/ceval.c:4166
#17 0x00005555556c9d29 in fast_function (func=func@entry=0x7ffee36b14a8, stack=<optimized out>, nargs=nargs@entry=2, 
    kwnames=kwnames@entry=0x0) at Python/ceval.c:4968
#18 0x00005555556ca01c in call_function (pp_stack=pp_stack@entry=0x7fffffff9c50, oparg=oparg@entry=2, kwnames=kwnames@entry=0x0)
    at Python/ceval.c:4872
#19 0x00005555556d47e5 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3335
#20 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x55555859d5f8, throwflag=throwflag@entry=0) at Python/ceval.c:754
#21 0x00005555556c90b5 in _PyFunction_FastCall (co=co@entry=0x7ffee368a100, args=0x7fffffff9dd8, args@entry=0x7fffffff9dc0, 
    nargs=nargs@entry=3, globals=globals@entry=0x7ffee36ff8c8) at Python/ceval.c:4933
#22 0x00005555556d6766 in _PyFunction_FastCallDict (func=func@entry=0x7ffee36acbd8, args=args@entry=0x7fffffff9dc0, 
    nargs=nargs@entry=3, kwargs=kwargs@entry=0x0) at Python/ceval.c:5035
#23 0x00005555555d7377 in _PyObject_FastCallDict (func=func@entry=0x7ffee36acbd8, args=args@entry=0x7fffffff9dc0, nargs=nargs@entry=3, 
    kwargs=kwargs@entry=0x0) at Objects/abstract.c:2310
#24 0x00005555555d7629 in _PyObject_Call_Prepend (func=0x7ffee36acbd8, obj=obj@entry=0x7ffee36b2058, args=0x7fff848ee218, kwargs=0x0)
    at Objects/abstract.c:2373
#25 0x00005555555f3375 in method_call (method=<optimized out>, args=<optimized out>, kwargs=<optimized out>)
    at Objects/classobject.c:314
#26 0x00005555555d7017 in PyObject_Call (func=func@entry=0x7ffee336e678, args=args@entry=0x7fff848ee218, kwargs=kwargs@entry=0x0)
    at Objects/abstract.c:2261
#27 0x000055555564dbe5 in slot_tp_call (self=self@entry=0x7ffee36b2058, args=args@entry=0x7fff848ee218, kwds=kwds@entry=0x0)
    at Objects/typeobject.c:6207
#28 0x00005555555d723e in _PyObject_FastCallDict (func=func@entry=0x7ffee36b2058, args=args@entry=0x5555585eb080, nargs=nargs@entry=2, 
    kwargs=kwargs@entry=0x0) at Objects/abstract.c:2331
#29 0x00005555555d7a0c in _PyObject_FastCallKeywords (func=func@entry=0x7ffee36b2058, stack=0x5555585eb080, nargs=nargs@entry=2, 
    kwnames=kwnames@entry=0x0) at Objects/abstract.c:2496
#30 0x00005555556c9de6 in call_function (pp_stack=pp_stack@entry=0x7fffffffa000, oparg=oparg@entry=2, kwnames=kwnames@entry=0x0)
    at Python/ceval.c:4875
#31 0x00005555556d47e5 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3335
#32 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x5555585eaec8, throwflag=throwflag@entry=0) at Python/ceval.c:754
#33 0x00005555556c90b5 in _PyFunction_FastCall (co=<optimized out>, args=0x555558706208, nargs=nargs@entry=2, globals=<optimized out>)
    at Python/ceval.c:4933
#34 0x00005555556c9cf5 in fast_function (func=func@entry=0x7ffee36b0280, stack=<optimized out>, nargs=nargs@entry=2, 
    kwnames=kwnames@entry=0x0) at Python/ceval.c:4968
#35 0x00005555556ca01c in call_function (pp_stack=pp_stack@entry=0x7fffffffa1c0, oparg=oparg@entry=2, kwnames=kwnames@entry=0x0)
    at Python/ceval.c:4872
#36 0x00005555556d47e5 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3335
#37 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x555558706048, throwflag=throwflag@entry=0) at Python/ceval.c:754
#38 0x00005555556c90b5 in _PyFunction_FastCall (co=co@entry=0x7ffee368a100, args=0x7fffffffa348, args@entry=0x7fffffffa330, 
    nargs=nargs@entry=3, globals=globals@entry=0x7ffee36ff8c8) at Python/ceval.c:4933
#39 0x00005555556d6766 in _PyFunction_FastCallDict (func=func@entry=0x7ffee36acbd8, args=args@entry=0x7fffffffa330, 
    nargs=nargs@entry=3, kwargs=kwargs@entry=0x0) at Python/ceval.c:5035
#40 0x00005555555d7377 in _PyObject_FastCallDict (func=func@entry=0x7ffee36acbd8, args=args@entry=0x7fffffffa330, nargs=nargs@entry=3, 
    kwargs=kwargs@entry=0x0) at Objects/abstract.c:2310
#41 0x00005555555d7629 in _PyObject_Call_Prepend (func=0x7ffee36acbd8, obj=obj@entry=0x7ffee36b20c0, args=0x7fff848ee678, kwargs=0x0)
    at Objects/abstract.c:2373
#42 0x00005555555f3375 in method_call (method=<optimized out>, args=<optimized out>, kwargs=<optimized out>)
    at Objects/classobject.c:314
#43 0x00005555555d7017 in PyObject_Call (func=func@entry=0x7fffea401c28, args=args@entry=0x7fff848ee678, kwargs=kwargs@entry=0x0)
    at Objects/abstract.c:2261
--Type <RET> for more, q to quit, c to continue without paging--
#44 0x000055555564dbe5 in slot_tp_call (self=self@entry=0x7ffee36b20c0, args=args@entry=0x7fff848ee678, kwds=kwds@entry=0x0)
    at Objects/typeobject.c:6207
#45 0x00005555555d723e in _PyObject_FastCallDict (func=func@entry=0x7ffee36b20c0, args=args@entry=0x5555585cf1c0, nargs=nargs@entry=2, 
    kwargs=kwargs@entry=0x0) at Objects/abstract.c:2331
#46 0x00005555555d7a0c in _PyObject_FastCallKeywords (func=func@entry=0x7ffee36b20c0, stack=0x5555585cf1c0, nargs=nargs@entry=2, 
    kwnames=kwnames@entry=0x0) at Objects/abstract.c:2496
#47 0x00005555556c9de6 in call_function (pp_stack=pp_stack@entry=0x7fffffffa570, oparg=oparg@entry=2, kwnames=kwnames@entry=0x0)
    at Python/ceval.c:4875
#48 0x00005555556d47e5 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3335
#49 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x5555585cf008, throwflag=throwflag@entry=0) at Python/ceval.c:754
#50 0x00005555556c9ac6 in _PyEval_EvalCodeWithName (_co=0x7ffee3704a00, globals=<optimized out>, locals=locals@entry=0x0, 
    args=<optimized out>, argcount=1, kwnames=0x0, kwargs=0x555558636858, kwcount=0, kwstep=1, defs=0x0, defcount=0, kwdefs=0x0, 
    closure=0x7fff84936ae8, name=0x7ffee37072e0, qualname=0x7ffee36fab40) at Python/ceval.c:4166
#51 0x00005555556c9d29 in fast_function (func=func@entry=0x7fff848b5a68, stack=<optimized out>, nargs=nargs@entry=1, 
    kwnames=kwnames@entry=0x0) at Python/ceval.c:4968
#52 0x00005555556ca01c in call_function (pp_stack=pp_stack@entry=0x7fffffffa7f0, oparg=oparg@entry=1, kwnames=kwnames@entry=0x0)
    at Python/ceval.c:4872
#53 0x00005555556d47e5 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3335
#54 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x5555586366a8, throwflag=throwflag@entry=0) at Python/ceval.c:754
#55 0x00005555556c9ac6 in _PyEval_EvalCodeWithName (_co=0x7ffee3704ac0, globals=<optimized out>, locals=locals@entry=0x0, 
    args=<optimized out>, argcount=2, kwnames=0x0, kwargs=0x5555578a3a00, kwcount=0, kwstep=1, defs=0x0, defcount=0, kwdefs=0x0, 
    closure=0x0, name=0x7ffee37075f0, qualname=0x7ffee37075f0) at Python/ceval.c:4166
#56 0x00005555556c9d29 in fast_function (func=func@entry=0x7ffee36ac840, stack=<optimized out>, nargs=nargs@entry=2, 
    kwnames=kwnames@entry=0x0) at Python/ceval.c:4968
#57 0x00005555556ca01c in call_function (pp_stack=pp_stack@entry=0x7fffffffaa70, oparg=oparg@entry=2, kwnames=kwnames@entry=0x0)
    at Python/ceval.c:4872
#58 0x00005555556d47e5 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3335
#59 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x5555578a37e8, throwflag=throwflag@entry=0) at Python/ceval.c:754
#60 0x00005555556c9ac6 in _PyEval_EvalCodeWithName (_co=0x7ffee368a4c0, globals=<optimized out>, locals=locals@entry=0x0, 
    args=<optimized out>, argcount=4, kwnames=0x7ffee3705e50, kwargs=0x5555577b3980, kwcount=1, kwstep=1, defs=0x7ffee369c358, 
    defcount=1, kwdefs=0x0, closure=0x0, name=0x7ffee37079e0, qualname=0x7ffee37079e0) at Python/ceval.c:4166
#61 0x00005555556c9d29 in fast_function (func=func@entry=0x7ffee36acc90, stack=<optimized out>, nargs=nargs@entry=4, 
    kwnames=kwnames@entry=0x7ffee3705e28) at Python/ceval.c:4968
#62 0x00005555556ca01c in call_function (pp_stack=pp_stack@entry=0x7fffffffacf8, oparg=oparg@entry=5, 
    kwnames=kwnames@entry=0x7ffee3705e28) at Python/ceval.c:4872
#63 0x00005555556d4902 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3351
#64 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x5555577b3758, throwflag=throwflag@entry=0) at Python/ceval.c:754
#65 0x00005555556c9ac6 in _PyEval_EvalCodeWithName (_co=0x7ffee368a040, globals=<optimized out>, locals=locals@entry=0x0, 
    args=<optimized out>, argcount=2, kwnames=0x0, kwargs=0x5555585cc468, kwcount=0, kwstep=1, defs=0x7ffee369c2f0, defcount=1, 
    kwdefs=0x0, closure=0x0, name=0x7ffff3acdc10, qualname=0x7ffff3acdc10) at Python/ceval.c:4166
#66 0x00005555556c9d29 in fast_function (func=func@entry=0x7ffee36aca68, stack=<optimized out>, nargs=nargs@entry=2, 
    kwnames=kwnames@entry=0x0) at Python/ceval.c:4968
#67 0x00005555556ca01c in call_function (pp_stack=pp_stack@entry=0x7fffffffaf70, oparg=oparg@entry=2, kwnames=kwnames@entry=0x0)
    at Python/ceval.c:4872
#68 0x00005555556d47e5 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3335
#69 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x5555585cc288, throwflag=throwflag@entry=0) at Python/ceval.c:754
#70 0x00005555556c9ac6 in _PyEval_EvalCodeWithName (_co=0x7ffee36f2280, globals=<optimized out>, locals=locals@entry=0x0, 
    args=<optimized out>, argcount=1, kwnames=0x0, kwargs=0x5555586dfb30, kwcount=0, kwstep=1, defs=0x7ffee36f0ad0, defcount=3, 
    kwdefs=0x0, closure=0x0, name=0x7ffff3b65ba0, qualname=0x7ffff3b65ba0) at Python/ceval.c:4166
#71 0x00005555556c9d29 in fast_function (func=func@entry=0x7ffee364e560, stack=<optimized out>, nargs=nargs@entry=1, 
    kwnames=kwnames@entry=0x0) at Python/ceval.c:4968
#72 0x00005555556ca01c in call_function (pp_stack=pp_stack@entry=0x7fffffffb1f0, oparg=oparg@entry=1, kwnames=kwnames@entry=0x0)
    at Python/ceval.c:4872
#73 0x00005555556d47e5 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3335
#74 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x5555586df978, throwflag=throwflag@entry=0) at Python/ceval.c:754
#75 0x00005555556c90b5 in _PyFunction_FastCall (co=<optimized out>, args=0x55555789b3e8, nargs=nargs@entry=1, globals=<optimized out>)
    at Python/ceval.c:4933
#76 0x00005555556c9cf5 in fast_function (func=func@entry=0x7ffff3d77338, stack=<optimized out>, nargs=nargs@entry=1, 
    kwnames=kwnames@entry=0x0) at Python/ceval.c:4968
#77 0x00005555556ca01c in call_function (pp_stack=pp_stack@entry=0x7fffffffb3b0, oparg=oparg@entry=0, kwnames=kwnames@entry=0x0)
    at Python/ceval.c:4872
#78 0x00005555556d47e5 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3335
#79 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x55555789b1e8, throwflag=throwflag@entry=0) at Python/ceval.c:754
#80 0x00005555556c9ac6 in _PyEval_EvalCodeWithName (_co=_co@entry=0x7ffff4793d00, globals=globals@entry=0x7ffff47f06e8, 
    locals=locals@entry=0x0, args=args@entry=0x7fffffffb5e0, argcount=argcount@entry=2, kwnames=kwnames@entry=0x7ffff6e24080, 
    kwargs=0x7ffff6e24088, kwcount=0, kwstep=2, defs=0x7ffff47a71b8, defcount=1, kwdefs=0x0, closure=0x0, name=0x7ffff6aff728, 
    qualname=0x7ffff4790f20) at Python/ceval.c:4166
#81 0x00005555556d67e6 in _PyFunction_FastCallDict (func=func@entry=0x7ffff4729eb8, args=args@entry=0x7fffffffb5e0, 
    nargs=nargs@entry=2, kwargs=kwargs@entry=0x7fffea67e058) at Python/ceval.c:5084
#82 0x00005555555d7377 in _PyObject_FastCallDict (func=func@entry=0x7ffff4729eb8, args=args@entry=0x7fffffffb5e0, nargs=nargs@entry=2, 
    kwargs=kwargs@entry=0x7fffea67e058) at Objects/abstract.c:2310
#83 0x00005555555d7629 in _PyObject_Call_Prepend (func=0x7ffff4729eb8, obj=obj@entry=0x7fffea67b7a8, args=0x7fffea43b0c0, 
    kwargs=0x7fffea67e058) at Objects/abstract.c:2373
--Type <RET> for more, q to quit, c to continue without paging--
#84 0x00005555555f3375 in method_call (method=<optimized out>, args=<optimized out>, kwargs=<optimized out>)
    at Objects/classobject.c:314
#85 0x00005555555d7017 in PyObject_Call (func=func@entry=0x7ffee32d1b48, args=args@entry=0x7fffea43b0c0, 
    kwargs=kwargs@entry=0x7fffea67e058) at Objects/abstract.c:2261
#86 0x00005555556c82c7 in do_call_core (func=func@entry=0x7ffee32d1b48, callargs=callargs@entry=0x7fffea43b0c0, 
    kwdict=kwdict@entry=0x7fffea67e058) at Python/ceval.c:5120
#87 0x00005555556d4c75 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3404
#88 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x7fffea43d448, throwflag=throwflag@entry=0) at Python/ceval.c:754
#89 0x00005555556c9ac6 in _PyEval_EvalCodeWithName (_co=_co@entry=0x7ffff4793e80, globals=globals@entry=0x7ffff47f06e8, 
    locals=locals@entry=0x0, args=args@entry=0x7fffffffb9a0, argcount=argcount@entry=2, kwnames=kwnames@entry=0x0, kwargs=0x0, 
    kwcount=0, kwstep=2, defs=0x0, defcount=0, kwdefs=0x0, closure=0x0, name=0x7ffff6e27270, qualname=0x7ffff4791e50)
    at Python/ceval.c:4166
#90 0x00005555556d67e6 in _PyFunction_FastCallDict (func=func@entry=0x7ffff472b058, args=args@entry=0x7fffffffb9a0, 
    nargs=nargs@entry=2, kwargs=kwargs@entry=0x0) at Python/ceval.c:5084
#91 0x00005555555d7377 in _PyObject_FastCallDict (func=func@entry=0x7ffff472b058, args=args@entry=0x7fffffffb9a0, nargs=nargs@entry=2, 
    kwargs=kwargs@entry=0x0) at Objects/abstract.c:2310
#92 0x00005555555d7629 in _PyObject_Call_Prepend (func=0x7ffff472b058, obj=obj@entry=0x7fffea67b7a8, args=0x7fffea43b190, kwargs=0x0)
    at Objects/abstract.c:2373
#93 0x00005555555f3375 in method_call (method=<optimized out>, args=<optimized out>, kwargs=<optimized out>)
    at Objects/classobject.c:314
#94 0x00005555555d7017 in PyObject_Call (func=func@entry=0x7ffee32d9528, args=args@entry=0x7fffea43b190, kwargs=kwargs@entry=0x0)
    at Objects/abstract.c:2261
#95 0x000055555564dbe5 in slot_tp_call (self=self@entry=0x7fffea67b7a8, args=args@entry=0x7fffea43b190, kwds=kwds@entry=0x0)
    at Objects/typeobject.c:6207
#96 0x00005555555d723e in _PyObject_FastCallDict (func=func@entry=0x7fffea67b7a8, args=args@entry=0x555557e76160, nargs=nargs@entry=1, 
    kwargs=kwargs@entry=0x0) at Objects/abstract.c:2331
#97 0x00005555555d7a0c in _PyObject_FastCallKeywords (func=func@entry=0x7fffea67b7a8, stack=0x555557e76160, nargs=nargs@entry=1, 
    kwnames=kwnames@entry=0x0) at Objects/abstract.c:2496
#98 0x00005555556c9de6 in call_function (pp_stack=pp_stack@entry=0x7fffffffbbe0, oparg=oparg@entry=1, kwnames=kwnames@entry=0x0)
    at Python/ceval.c:4875
#99 0x00005555556d47e5 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3335
#100 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x555557e75f98, throwflag=throwflag@entry=0) at Python/ceval.c:754
#101 0x00005555556c9ac6 in _PyEval_EvalCodeWithName (_co=_co@entry=0x7ffff47ac280, globals=globals@entry=0x7ffff47fddf0, 
    locals=locals@entry=0x0, args=args@entry=0x7fffffffbe10, argcount=argcount@entry=2, kwnames=kwnames@entry=0x7ffff6e24080, 
    kwargs=0x7ffff6e24088, kwcount=0, kwstep=2, defs=0x7ffff47429d8, defcount=1, kwdefs=0x0, closure=0x0, name=0x7ffff6aff728, 
    qualname=0x7ffff47285f0) at Python/ceval.c:4166
#102 0x00005555556d67e6 in _PyFunction_FastCallDict (func=func@entry=0x7ffff472db20, args=args@entry=0x7fffffffbe10, 
    nargs=nargs@entry=2, kwargs=kwargs@entry=0x7fffea6766e8) at Python/ceval.c:5084
#103 0x00005555555d7377 in _PyObject_FastCallDict (func=func@entry=0x7ffff472db20, args=args@entry=0x7fffffffbe10, 
    nargs=nargs@entry=2, kwargs=kwargs@entry=0x7fffea6766e8) at Objects/abstract.c:2310
#104 0x00005555555d7629 in _PyObject_Call_Prepend (func=0x7ffff472db20, obj=obj@entry=0x7fffea67b538, args=0x7fffea6e3ef8, 
    kwargs=0x7fffea6766e8) at Objects/abstract.c:2373
#105 0x00005555555f3375 in method_call (method=<optimized out>, args=<optimized out>, kwargs=<optimized out>)
    at Objects/classobject.c:314
#106 0x00005555555d7017 in PyObject_Call (func=func@entry=0x7ffff5c4b988, args=args@entry=0x7fffea6e3ef8, 
    kwargs=kwargs@entry=0x7fffea6766e8) at Objects/abstract.c:2261
#107 0x00005555556c82c7 in do_call_core (func=func@entry=0x7ffff5c4b988, callargs=callargs@entry=0x7fffea6e3ef8, 
    kwdict=kwdict@entry=0x7fffea6766e8) at Python/ceval.c:5120
#108 0x00005555556d4c75 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3404
#109 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x7fffea9bde20, throwflag=throwflag@entry=0) at Python/ceval.c:754
#110 0x00005555556c9ac6 in _PyEval_EvalCodeWithName (_co=_co@entry=0x7ffff47a6c40, globals=globals@entry=0x7ffff47fddf0, 
    locals=locals@entry=0x0, args=args@entry=0x7fffffffc1d0, argcount=argcount@entry=2, kwnames=kwnames@entry=0x0, kwargs=0x0, 
    kwcount=0, kwstep=2, defs=0x0, defcount=0, kwdefs=0x0, closure=0x0, name=0x7ffff6e27270, qualname=0x7ffff472e130)
    at Python/ceval.c:4166
#111 0x00005555556d67e6 in _PyFunction_FastCallDict (func=func@entry=0x7ffff472d9b0, args=args@entry=0x7fffffffc1d0, 
    nargs=nargs@entry=2, kwargs=kwargs@entry=0x0) at Python/ceval.c:5084
#112 0x00005555555d7377 in _PyObject_FastCallDict (func=func@entry=0x7ffff472d9b0, args=args@entry=0x7fffffffc1d0, 
    nargs=nargs@entry=2, kwargs=kwargs@entry=0x0) at Objects/abstract.c:2310
#113 0x00005555555d7629 in _PyObject_Call_Prepend (func=0x7ffff472d9b0, obj=obj@entry=0x7fffea67b538, args=0x7fffea6ceae8, kwargs=0x0)
    at Objects/abstract.c:2373
#114 0x00005555555f3375 in method_call (method=<optimized out>, args=<optimized out>, kwargs=<optimized out>)
    at Objects/classobject.c:314
#115 0x00005555555d7017 in PyObject_Call (func=func@entry=0x7ffee335b7c8, args=args@entry=0x7fffea6ceae8, kwargs=kwargs@entry=0x0)
    at Objects/abstract.c:2261
#116 0x000055555564dbe5 in slot_tp_call (self=self@entry=0x7fffea67b538, args=args@entry=0x7fffea6ceae8, kwds=kwds@entry=0x0)
    at Objects/typeobject.c:6207
#117 0x00005555555d723e in _PyObject_FastCallDict (func=func@entry=0x7fffea67b538, args=args@entry=0x555557e75930, 
    nargs=nargs@entry=1, kwargs=kwargs@entry=0x0) at Objects/abstract.c:2331
#118 0x00005555555d7a0c in _PyObject_FastCallKeywords (func=func@entry=0x7fffea67b538, stack=0x555557e75930, nargs=nargs@entry=1, 
    kwnames=kwnames@entry=0x0) at Objects/abstract.c:2496
#119 0x00005555556c9de6 in call_function (pp_stack=pp_stack@entry=0x7fffffffc410, oparg=oparg@entry=1, kwnames=kwnames@entry=0x0)
    at Python/ceval.c:4875
#120 0x00005555556d47e5 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3335
--Type <RET> for more, q to quit, c to continue without paging--
#121 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x555557e75768, throwflag=throwflag@entry=0) at Python/ceval.c:754
#122 0x00005555556c9ac6 in _PyEval_EvalCodeWithName (_co=_co@entry=0x7ffff47ac280, globals=globals@entry=0x7ffff47fddf0, 
    locals=locals@entry=0x0, args=args@entry=0x7fffffffc640, argcount=argcount@entry=2, kwnames=kwnames@entry=0x7ffff6e24080, 
    kwargs=0x7ffff6e24088, kwcount=0, kwstep=2, defs=0x7ffff47429d8, defcount=1, kwdefs=0x0, closure=0x0, name=0x7ffff6aff728, 
    qualname=0x7ffff47285f0) at Python/ceval.c:4166
#123 0x00005555556d67e6 in _PyFunction_FastCallDict (func=func@entry=0x7ffff472db20, args=args@entry=0x7fffffffc640, 
    nargs=nargs@entry=2, kwargs=kwargs@entry=0x7fffea43c1c0) at Python/ceval.c:5084
#124 0x00005555555d7377 in _PyObject_FastCallDict (func=func@entry=0x7ffff472db20, args=args@entry=0x7fffffffc640, 
    nargs=nargs@entry=2, kwargs=kwargs@entry=0x7fffea43c1c0) at Objects/abstract.c:2310
#125 0x00005555555d7629 in _PyObject_Call_Prepend (func=0x7ffff472db20, obj=obj@entry=0x7fffea9376d8, args=0x7fffea6cea18, 
    kwargs=0x7fffea43c1c0) at Objects/abstract.c:2373
#126 0x00005555555f3375 in method_call (method=<optimized out>, args=<optimized out>, kwargs=<optimized out>)
    at Objects/classobject.c:314
#127 0x00005555555d7017 in PyObject_Call (func=func@entry=0x7ffff5d44fa8, args=args@entry=0x7fffea6cea18, 
    kwargs=kwargs@entry=0x7fffea43c1c0) at Objects/abstract.c:2261
#128 0x00005555556c82c7 in do_call_core (func=func@entry=0x7ffff5d44fa8, callargs=callargs@entry=0x7fffea6cea18, 
    kwdict=kwdict@entry=0x7fffea43c1c0) at Python/ceval.c:5120
#129 0x00005555556d4c75 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3404
#130 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x7fffea9bdc28, throwflag=throwflag@entry=0) at Python/ceval.c:754
#131 0x00005555556c9ac6 in _PyEval_EvalCodeWithName (_co=_co@entry=0x7ffff47a6c40, globals=globals@entry=0x7ffff47fddf0, 
    locals=locals@entry=0x0, args=args@entry=0x7fffffffca00, argcount=argcount@entry=2, kwnames=kwnames@entry=0x0, kwargs=0x0, 
    kwcount=0, kwstep=2, defs=0x0, defcount=0, kwdefs=0x0, closure=0x0, name=0x7ffff6e27270, qualname=0x7ffff472e130)
    at Python/ceval.c:4166
#132 0x00005555556d67e6 in _PyFunction_FastCallDict (func=func@entry=0x7ffff472d9b0, args=args@entry=0x7fffffffca00, 
    nargs=nargs@entry=2, kwargs=kwargs@entry=0x0) at Python/ceval.c:5084
#133 0x00005555555d7377 in _PyObject_FastCallDict (func=func@entry=0x7ffff472d9b0, args=args@entry=0x7fffffffca00, 
    nargs=nargs@entry=2, kwargs=kwargs@entry=0x0) at Objects/abstract.c:2310
#134 0x00005555555d7629 in _PyObject_Call_Prepend (func=0x7ffff472d9b0, obj=obj@entry=0x7fffea9376d8, args=0x7fffea6ce9b0, kwargs=0x0)
    at Objects/abstract.c:2373
#135 0x00005555555f3375 in method_call (method=<optimized out>, args=<optimized out>, kwargs=<optimized out>)
    at Objects/classobject.c:314
#136 0x00005555555d7017 in PyObject_Call (func=func@entry=0x7ffee341b9f8, args=args@entry=0x7fffea6ce9b0, kwargs=kwargs@entry=0x0)
    at Objects/abstract.c:2261
#137 0x000055555564dbe5 in slot_tp_call (self=self@entry=0x7fffea9376d8, args=args@entry=0x7fffea6ce9b0, kwds=kwds@entry=0x0)
    at Objects/typeobject.c:6207
#138 0x00005555555d723e in _PyObject_FastCallDict (func=func@entry=0x7fffea9376d8, args=args@entry=0x555557e87770, 
    nargs=nargs@entry=1, kwargs=kwargs@entry=0x0) at Objects/abstract.c:2331
#139 0x00005555555d7a0c in _PyObject_FastCallKeywords (func=func@entry=0x7fffea9376d8, stack=0x555557e87770, nargs=nargs@entry=1, 
    kwnames=kwnames@entry=0x0) at Objects/abstract.c:2496
#140 0x00005555556c9de6 in call_function (pp_stack=pp_stack@entry=0x7fffffffcc40, oparg=oparg@entry=1, kwnames=kwnames@entry=0x0)
    at Python/ceval.c:4875
#141 0x00005555556d47e5 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3335
#142 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x555557e87558, throwflag=throwflag@entry=0) at Python/ceval.c:754
#143 0x00005555556c90b5 in _PyFunction_FastCall (co=<optimized out>, args=0x555557e88a80, nargs=nargs@entry=2, globals=<optimized out>)
    at Python/ceval.c:4933
#144 0x00005555556c9cf5 in fast_function (func=func@entry=0x7ffff46606d0, stack=<optimized out>, nargs=nargs@entry=2, 
    kwnames=kwnames@entry=0x0) at Python/ceval.c:4968
#145 0x00005555556ca01c in call_function (pp_stack=pp_stack@entry=0x7fffffffce00, oparg=oparg@entry=1, kwnames=kwnames@entry=0x0)
    at Python/ceval.c:4872
#146 0x00005555556d47e5 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3335
#147 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x555557e888d8, throwflag=throwflag@entry=0) at Python/ceval.c:754
#148 0x00005555556c90b5 in _PyFunction_FastCall (co=<optimized out>, args=0x5555577353a8, nargs=nargs@entry=1, globals=<optimized out>)
    at Python/ceval.c:4933
#149 0x00005555556c9cf5 in fast_function (func=func@entry=0x7ffff4661058, stack=<optimized out>, nargs=nargs@entry=1, 
    kwnames=kwnames@entry=0x0) at Python/ceval.c:4968
#150 0x00005555556ca01c in call_function (pp_stack=pp_stack@entry=0x7fffffffcfc0, oparg=oparg@entry=0, kwnames=kwnames@entry=0x0)
    at Python/ceval.c:4872
#151 0x00005555556d47e5 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3335
#152 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x5555577351a8, throwflag=throwflag@entry=0) at Python/ceval.c:754
#153 0x00005555556c9ac6 in _PyEval_EvalCodeWithName (_co=_co@entry=0x7ffff4737dc0, globals=globals@entry=0x7ffff47272b0, 
    locals=locals@entry=0x0, args=args@entry=0x7fffffffd1f0, argcount=argcount@entry=1, kwnames=kwnames@entry=0x7fffeaa8c4e0, 
    kwargs=0x7fffeaa8c4e8, kwcount=2, kwstep=2, defs=0x7ffff4660868, defcount=11, kwdefs=0x7ffff4747148, closure=0x0, 
    name=0x7ffff6e27430, qualname=0x7ffff473f7c0) at Python/ceval.c:4166
#154 0x00005555556d67e6 in _PyFunction_FastCallDict (func=func@entry=0x7ffff46608f8, args=args@entry=0x7fffffffd1f0, 
    nargs=nargs@entry=1, kwargs=kwargs@entry=0x7fffea6db580) at Python/ceval.c:5084
#155 0x00005555555d7377 in _PyObject_FastCallDict (func=func@entry=0x7ffff46608f8, args=args@entry=0x7fffffffd1f0, 
    nargs=nargs@entry=1, kwargs=kwargs@entry=0x7fffea6db580) at Objects/abstract.c:2310
#156 0x00005555555d7629 in _PyObject_Call_Prepend (func=0x7ffff46608f8, obj=obj@entry=0x7fffeaa58330, args=0x7ffff6e24058, 
    kwargs=0x7fffea6db580) at Objects/abstract.c:2373
#157 0x00005555555f3375 in method_call (method=<optimized out>, args=<optimized out>, kwargs=<optimized out>)
    at Objects/classobject.c:314
#158 0x00005555555d7017 in PyObject_Call (func=func@entry=0x7ffff5bb2598, args=args@entry=0x7ffff6e24058, 
    kwargs=kwargs@entry=0x7fffea6db580) at Objects/abstract.c:2261
--Type <RET> for more, q to quit, c to continue without paging--
#159 0x000055555564d7f3 in slot_tp_init (self=<optimized out>, args=0x7ffff6e24058, kwds=0x7fffea6db580) at Objects/typeobject.c:6420
#160 0x0000555555648f92 in type_call (type=type@entry=0x5555571f2158, args=args@entry=0x7ffff6e24058, kwds=kwds@entry=0x7fffea6db580)
    at Objects/typeobject.c:915
#161 0x00005555555d723e in _PyObject_FastCallDict (func=func@entry=0x5555571f2158, args=args@entry=0x555557e6d168, 
    nargs=nargs@entry=0, kwargs=kwargs@entry=0x7fffea6db580) at Objects/abstract.c:2331
#162 0x00005555555d7a0c in _PyObject_FastCallKeywords (func=func@entry=0x5555571f2158, stack=0x555557e6d168, nargs=nargs@entry=0, 
    kwnames=kwnames@entry=0x7ffee2ecf948) at Objects/abstract.c:2496
#163 0x00005555556c9de6 in call_function (pp_stack=pp_stack@entry=0x7fffffffd478, oparg=oparg@entry=1, 
    kwnames=kwnames@entry=0x7ffee2ecf948) at Python/ceval.c:4875
#164 0x00005555556d4902 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3351
#165 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x555557e6cf48, throwflag=throwflag@entry=0) at Python/ceval.c:754
#166 0x00005555556c90b5 in _PyFunction_FastCall (co=<optimized out>, args=0x7ffee2e9ed88, nargs=1, globals=<optimized out>)
    at Python/ceval.c:4933
#167 0x00005555556c9cdc in fast_function (func=func@entry=0x7ffee2e233f0, stack=<optimized out>, nargs=nargs@entry=0, 
    kwnames=kwnames@entry=0x0) at Python/ceval.c:4975
#168 0x00005555556ca01c in call_function (pp_stack=pp_stack@entry=0x7fffffffd630, oparg=oparg@entry=0, kwnames=kwnames@entry=0x0)
    at Python/ceval.c:4872
#169 0x00005555556d47e5 in _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3335
#170 0x00005555556c8fd5 in PyEval_EvalFrameEx (f=f@entry=0x555555a07378, throwflag=throwflag@entry=0) at Python/ceval.c:754
#171 0x00005555556c9ac6 in _PyEval_EvalCodeWithName (_co=0x7ffff6736a00, globals=<optimized out>, locals=<optimized out>, 
    args=<optimized out>, argcount=argcount@entry=0, kwnames=0x0, kwargs=0x0, kwcount=0, kwstep=2, defs=0x0, defcount=0, kwdefs=0x0, 
    closure=0x0, name=0x0, qualname=0x0) at Python/ceval.c:4166
#172 0x00005555556ca109 in PyEval_EvalCodeEx (_co=_co@entry=0x7ffff6736a00, globals=globals@entry=0x7ffff6d2db20, 
    locals=locals@entry=0x7ffff6d2db20, args=args@entry=0x0, argcount=argcount@entry=0, kws=kws@entry=0x0, kwcount=0, defs=0x0, 
    defcount=0, kwdefs=0x0, closure=0x0) at Python/ceval.c:4187
#173 0x00005555556ca13b in PyEval_EvalCode (co=co@entry=0x7ffff6736a00, globals=globals@entry=0x7ffff6d2db20, 
    locals=locals@entry=0x7ffff6d2db20) at Python/ceval.c:731
#174 0x00005555555b1639 in run_mod (mod=mod@entry=0x555555d1e520, filename=filename@entry=0x7ffff6a4b820, 
    globals=globals@entry=0x7ffff6d2db20, locals=locals@entry=0x7ffff6d2db20, flags=flags@entry=0x7fffffffd94c, 
    arena=arena@entry=0x7ffff6acfbe0) at Python/pythonrun.c:1025
#175 0x00005555555b45b0 in PyRun_FileExFlags (fp=fp@entry=0x5555558b38a0, 
    filename_str=filename_str@entry=0x7ffff6b1c5b0 "test_jit.py", start=start@entry=257, globals=globals@entry=0x7ffff6d2db20, 
    locals=locals@entry=0x7ffff6d2db20, closeit=closeit@entry=1, flags=0x7fffffffd94c) at Python/pythonrun.c:978
#176 0x00005555555b4937 in PyRun_SimpleFileExFlags (fp=fp@entry=0x5555558b38a0, filename=<optimized out>, 
    filename@entry=0x7ffff6b1c5b0 "test_jit.py", closeit=closeit@entry=1, flags=flags@entry=0x7fffffffd94c) at Python/pythonrun.c:419
#177 0x00005555555b4b16 in PyRun_AnyFileExFlags (fp=fp@entry=0x5555558b38a0, filename=0x7ffff6b1c5b0 "test_jit.py", 
    closeit=closeit@entry=1, flags=flags@entry=0x7fffffffd94c) at Python/pythonrun.c:81
#178 0x00005555555c51a2 in run_file (fp=fp@entry=0x5555558b38a0, filename=filename@entry=0x5555558a7750 L"test_jit.py", 
    p_cf=p_cf@entry=0x7fffffffd94c) at Modules/main.c:340
#179 0x00005555555c5dc7 in Py_Main (argc=3, argv=0x5555558a62a0) at Modules/main.c:810
#180 0x00005555555aabc2 in main (argc=3, argv=0x7fffffffdb68) at ./Programs/python.c:69
