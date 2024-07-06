RuntimeError:
Unknown type name '_size_4_t':
  File "/home/bowbao/repos/pytorch/torch/nn/modules/padding.py", line 453
    def __init__(self, padding: _size_4_t) -> None:
                                ~~~~~~~~~ <--- HERE
        super(ZeroPad2d, self).__init__(padding, 0.)
'ZeroPad2d.__init__' is being compiled since it was called from '__torch__.torch.nn.modules.padding.ZeroPad2d'
  File "repro_1p_rnn_fairseq.py", line 6
    def forward(self, x):
        pad_op =  nn.ZeroPad2d(padding=(10, 20, 0, 0))
                  ~~~~~~~~~~~~ <--- HERE
        return pad_op(x)
'__torch__.torch.nn.modules.padding.ZeroPad2d' is being compiled since it was called from 'Pad.forward'
  File "repro_1p_rnn_fairseq.py", line 6
    def forward(self, x):
        pad_op =  nn.ZeroPad2d(padding=(10, 20, 0, 0))
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ <--- HERE
        return pad_op(x)