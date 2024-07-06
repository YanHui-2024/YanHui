diff --git a/torch/nn/modules/rnn.py b/torch/nn/modules/rnn.py
index f94728653b..2320fc1f15 100644
@@ -731,7 +731,6 @@ class LSTM(RNNBase):
         if isinstance(orig_input, PackedSequence):
             input, batch_sizes, sorted_indices, unsorted_indices = input
             max_batch_size = batch_sizes[0]
-            max_batch_size = int(max_batch_size)
         else:
             batch_sizes = None
             assert (input.dim() in (2, 3)), f"LSTM: Expected input to be 2-D or 3-D but received {input.dim()}-D tensor"
@@ -739,7 +738,7 @@ class LSTM(RNNBase):
             batch_dim = 0 if self.batch_first else 1
             if not is_batched:
                 input = input.unsqueeze(batch_dim)
-            max_batch_size = input.size(0) if self.batch_first else input.size(1)
+            max_batch_size = torch.as_tensor(input.size(0) if self.batch_first else input.size(1))
             sorted_indices = None  
             unsorted_indices = None
 
@@ -922,7 +921,6 @@ class GRU(RNNBase):
         if isinstance(orig_input, PackedSequence):
             input, batch_sizes, sorted_indices, unsorted_indices = input
             max_batch_size = batch_sizes[0]
-            max_batch_size = int(max_batch_size)
         else:
             batch_sizes = None
             assert (input.dim() in (2, 3)), f"GRU: Expected input to be 2-D or 3-D but received {input.dim()}-D tensor"
@@ -939,7 +937,7 @@ class GRU(RNNBase):
                 if hx is not None and hx.dim() != 3:
                     raise RuntimeError(
                         f"For batched 3-D input, hx should also be 3-D but got {hx.dim()}-D tensor")
-            max_batch_size = input.size(0) if self.batch_first else input.size(1)
+            max_batch_size = torch.as_tensor(input.size(0) if self.batch_first else input.size(1))
             sorted_indices = None  
             unsorted_indices = None