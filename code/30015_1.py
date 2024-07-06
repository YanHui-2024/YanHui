---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
<ipython-input-66-6d725915459d> in <module>
     53 data = torch.Tensor(vue_clip_emb).view(1, -1, 100)
     54 lengths = torch.tensor([74])
---> 55 output = ts_model_multihead.forward(data=data, lengths=lengths)
     56 print(output)

RuntimeError: 


new_type INTERNAL ASSERT FAILED at caffe2/torch/csrc/jit/passes/shape_analysis.cpp:280, please report a bug to PyTorch. 
The above operation failed shape propagation in this context:
at /mnt/xarfuse/uid-156246/70539c06-ns-4026531840/torch/nn/functional.py:3312:12
                                                  dtype=attn_mask.dtype,
                                                  device=attn_mask.device)], dim=1)
            if key_padding_mask is not None:
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~...  <--- HERE
                key_padding_mask = torch.cat(
                    [key_padding_mask, torch.zeros((key_padding_mask.size(0), 1),

The above operation failed shape propagation in this context:
at /mnt/xarfuse/uid-156246/70539c06-ns-4026531840/torch/nn/functional.py:3303:4
    q = q * scaling

    if bias_k is not None and bias_v is not None:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~...  <--- HERE
        if static_k is None and static_v is None:
            k = torch.cat([k, bias_k.repeat(1, bsz, 1)])

The above operation failed shape propagation in this context:
at <ipython-input-60-415a6b53c56b>:127:8
          L is the target sequence length, S is the source sequence length.
        """
        if not self._qkv_same_embed_dim:
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~...  <--- HERE
            return nn.functional.multi_head_attention_forward(
                query, key, value, self.embed_dim, self.num_heads,