import torch
from torch import nn

x = torch.tensor([[[[ 1.1227, -0.5545, -0.7871,  0.0841,  0.3714,  0.1612],
          [-0.2052, -0.6623,  1.6033,  2.1245,  1.9609, -1.6847],
          [ 0.1736, -0.7240, -0.0737,  0.3207,  1.5287, -1.3479]],

         [[-0.0267,  1.3100, -0.5756,  0.9288,  1.0432, -0.4871],
          [-0.9110, -0.2054, -1.6963,  0.5995,  1.7877, -2.0397],
          [-0.1205, -1.0103, -2.1805,  1.4364, -1.3835,  0.6537]]]])

device = "mps"
x_m1 = x.to(device=device)
conv_m1 = nn.Sequential(
    nn.Conv2d(2, 2, stride=1, kernel_size=3),
    nn.BatchNorm2d(num_features=2)
).to(device=device)

y_m1 = conv_m1(x_m1)
conv_m1.eval()
eval_m1 = conv_m1(x_m1)

torch.jit.trace(conv_m1, x_m1)