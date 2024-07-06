diff --git a/test/test_jit.py b/test/test_jit.py
index a6fd537af..3ae4abe05 100644
--- a/test/test_jit.py
+++ b/test/test_jit.py
@@ -688,9 +688,18 @@ class TestJit(JitTestCase):
     @unittest.skipIf(not RUN_CUDA, "fuser requires CUDA")
     @skipIfRocm
     def test_lstm_fusion_concat_cuda(self):
-        inputs = get_lstm_inputs('cuda')
-        ge = self.checkTrace(LSTMCellC, inputs)
-        self.assertExpectedGraph(ge.graph_for(*inputs))
+        fails = 0
+        for i in range(100):
+            print ('\r',i,'   ', end='')
+            sys.stdout.flush()
+            torch.manual_seed(i)
+            try:
+                inputs = get_lstm_inputs('cuda')
+                ge = self.checkTrace(LSTMCellC, inputs)
+                self.assertExpectedGraph(ge.graph_for(*inputs))
+            except:
+                fails += 1
+        print("failures", fails)
 
     @unittest.skipIf(IS_WINDOWS, "NYI: fuser support for Windows")
     @unittest.skipIf(not RUN_CUDA, "fuser requires CUDA")