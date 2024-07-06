---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
<ipython-input-51-b5b4f0d5a0f4> in <module>
      9 x = torch.randn(3)
     10 traced_module = torch.jit.trace_module(module, {"f": torch.randn(3)})
---> 11 torch.jit.freeze(traced_module.eval(), preserved_attrs=["f"])

/opt/conda/envs/lab42/lib/python3.7/site-packages/torch/jit/_freeze.py in freeze(mod, preserved_attrs, optimize_numerics)
    117 
    118     preserved_methods = [x for x in preserved_attrs if mod._c._has_method(x)]
--> 119     run_frozen_optimizations(out, optimize_numerics, preserved_methods)
    120 
    121     return out

/opt/conda/envs/lab42/lib/python3.7/site-packages/torch/jit/_freeze.py in run_frozen_optimizations(mod, optimize_numerics, preserved_methods)
    165 
    166     """
--> 167     torch._C._jit_pass_optimize_frozen_graph(mod.graph, optimize_numerics)
    168 
    169     if preserved_methods is None:

/opt/conda/envs/lab42/lib/python3.7/site-packages/torch/jit/_script.py in graph(self)
    650             ``forward`` method. See :ref:`interpreting-graphs` for details.
    651             """
--> 652             return self._c._get_method("forward").graph
    653 
    654         @property

RuntimeError: Method 'forward' is not defined.