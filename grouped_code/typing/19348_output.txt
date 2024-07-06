$ python test.py
SomeScriptModule(
  (linear): WeakScriptModuleProxy()
  (conv2d): WeakScriptModuleProxy()
  (conv3d): WeakScriptModuleProxy()
  (gru): GRU(16, 16)
  (lstm): LSTM(16, 16)
) <class '__main__.SomeScriptModule'>
??????
WeakScriptModuleProxy() <class 'torch.jit.WeakScriptModuleProxy'>
??????
WeakScriptModuleProxy() <class 'torch.jit.WeakScriptModuleProxy'>
??????
WeakScriptModuleProxy() <class 'torch.jit.WeakScriptModuleProxy'>
??????
GRU(16, 16) <class 'torch.nn.modules.rnn.GRU'>
m is GRU
LSTM(16, 16) <class 'torch.nn.modules.rnn.LSTM'>
m is LSTM