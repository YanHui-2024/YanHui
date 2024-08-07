from nets.models import DigitModel
import torch
import os
import onnx

#load pretrained torch model
def load_model(model, pretrained_path, load_to_cpu):
    print('Loading pretrained model from {}'.format(pretrained_path))
    if load_to_cpu:
        pretrained_dict = torch.load(pretrained_path, map_location=lambda storage, loc: storage)
    else:
        device = torch.cuda.current_device()
        pretrained_dict = torch.load(pretrained_path, map_location=lambda storage, loc: storage.cuda(device))
    model.load_state_dict(pretrained_dict, strict=False)
    return model

#convert to onnx model
def pth_to_onnx(model,input_path, output_path):

    
    torch_model = load_model(model,input_path,True)  
    torch_model.eval()
    torch_model = torch.jit.script(torch_model)
    x=torch.randn(1,1,28,28, device="cuda")
    export_onnx_file = output_path  
    print(torch_model)
    # Note: the bug is here
    torch.onnx.export(torch_model,
                      x,
                      export_onnx_file,
                      verbose=True,
                      opset_version=9,  
                      do_constant_folding=True, 
                      input_names=["input"], 
                      output_names=["output"] ,
                      dynamic_axes={"input": {0: "batch_size"}, 
                                     "output": {0: "batch_size"}}
                      )

#DigitModel 
#@inproceedings{
#  anonymous2022unsupervised,
#  title={Unsupervised Federated Learning is Possible},
#  author={Anonymous},
#  booktitle={Submitted to The Tenth International Conference on Learning Representations},
#  year={2022},
#  url={https://openreview.net/forum?id=WHA8009laxu},
#  note={under review}
# }
import torch
import torch.nn as nn
import torch.nn.functional as func
import torchvision
class DigitModel(nn.Module):
    def __init__(self, class_num=10):
        super(DigitModel, self).__init__()
        self.class_num = class_num

        self.conv1 = nn.Conv2d(3, 64, 5, 1, 2)
        self.bn1 = nn.BatchNorm2d(64)
        self.conv2 = nn.Conv2d(64, 64, 5, 1, 2)
        self.bn2 = nn.BatchNorm2d(64)
        self.conv3 = nn.Conv2d(64, 128, 5, 1, 2)
        self.bn3 = nn.BatchNorm2d(128)

        self.fc1 = nn.Linear(6272, 2048)
        self.bn4 = nn.BatchNorm1d(2048)
        self.fc2 = nn.Linear(2048, 512)
        self.bn5 = nn.BatchNorm1d(512)

        self.fc3 = nn.Linear(512, class_num)

    def forward(self, x, Pi, priors_corr, prior_test):
        x = func.relu(self.bn1(self.conv1(x)))
        x = func.max_pool2d(x, 2)

        x = func.relu(self.bn2(self.conv2(x)))
        x = func.max_pool2d(x, 2)

        x = func.relu(self.bn3(self.conv3(x)))
        x = x.view(x.shape[0], -1)

        x = self.fc1(x)
        x = self.bn4(x)
        x = func.relu(x)

        x = self.fc2(x)
        x = self.bn5(x)
        x = func.relu(x)

        x = self.fc3(x)

        g = torch.softmax(x, dim=1)
        x = self.QfunctionMulticlass(g, Pi, priors_corr)

        return x

    def QfunctionMulticlass(self, g, Pi, priors_corr):
        pi_ita = torch.mm(Pi, g.permute(1, 0))
        rou_pi_ita = torch.matmul(priors_corr, pi_ita)

        pi_corr = pi_ita.permute(1, 0) * priors_corr.unsqueeze(0)
        output = (pi_corr.permute(1, 0) / rou_pi_ita).permute(1, 0)

        return output

    def predict(self, x):
        x = func.relu(self.bn1(self.conv1(x)))
        x = func.max_pool2d(x, 2)

        x = func.relu(self.bn2(self.conv2(x)))
        x = func.max_pool2d(x, 2)

        x = func.relu(self.bn3(self.conv3(x)))

        x = x.view(x.shape[0], -1)

        x = self.fc1(x)
        x = self.bn4(x)
        x = func.relu(x)

        x = self.fc2(x)
        x = self.bn5(x)
        x = func.relu(x)

        x = self.fc3(x)

        g = torch.softmax(x, dim=1)

        return g

#trackback
Traceback (most recent call last):
  File "D:/BaiduNetdiskDownload/FedUL/load_model.py", line 119, in <module>
    pth_to_onnx(model,input_path, onnx_path) 
  File "D:/BaiduNetdiskDownload/FedUL/load_model.py", line 35, in pth_to_onnx
    torch.onnx.export(torch_model,
  File "C:\tools\Anaconda3\envs\fedul\lib\site-packages\torch\onnx\__init__.py", line 316, in export
    return utils.export(model, args, f, export_params, verbose, training,
  File "C:\tools\Anaconda3\envs\fedul\lib\site-packages\torch\onnx\utils.py", line 107, in export
    _export(model, args, f, export_params, verbose, training, input_names, output_names,
  File "C:\tools\Anaconda3\envs\fedul\lib\site-packages\torch\onnx\utils.py", line 724, in _export
    _model_to_graph(model, args, verbose, input_names,
  File "C:\tools\Anaconda3\envs\fedul\lib\site-packages\torch\onnx\utils.py", line 493, in _model_to_graph
    graph, params, torch_out, module = _create_jit_graph(model, args)
  File "C:\tools\Anaconda3\envs\fedul\lib\site-packages\torch\onnx\utils.py", line 422, in _create_jit_graph
    graph = _propagate_and_assign_input_shapes(
RuntimeError: input_values.size() == param_count_list.size()INTERNAL ASSERT FAILED at "..\\torch\\csrc\\jit\\python\\script_init.cpp":480, please report a bug to PyTorch. 

Process finished with exit code 1
