diff --git a/aten/src/ATen/native/AdaptiveMaxPooling2d.cpp b/aten/src/ATen/native/AdaptiveMaxPooling2d.cpp
index b3b77c5..ec16c5e 100644
--- a/aten/src/ATen/native/AdaptiveMaxPooling2d.cpp
+++ b/aten/src/ATen/native/AdaptiveMaxPooling2d.cpp
@@ -322,6 +322,7 @@ std::tuple<Tensor, Tensor> adaptive_max_pool2d_cpu(
 {
   Tensor output = at::empty({0}, input.options());
   Tensor indices = at::empty({0}, input.options().dtype(kLong));
+  assert(output_size.size() == 2);
   adaptive_max_pool2d_out_cpu_template(
     output,
     indices,