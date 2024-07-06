class ModelThatNeedsDebugging(jit.ScriptModule)
  def __init__(self)
      ///
  def forward(self, x):
         y =  self.conv(x)
         y.save("./attention_input.pt")
         output = self.attention(y)
         output.save("./attention_feature_map.pt")
         return output