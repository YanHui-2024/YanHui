class YOLOv3(nn.Module):

    def __init__(self, anchors, anch_mask, n_classes, ignore_thre=0.7):
        """
        Initialization of YOLOv3 class.
        Args:
            config_model (dict): used in YOLOLayer.
            ignore_thre (float): used in YOLOLayer.
        """
        super(YOLOv3, self).__init__()
        self.loss_list = []
        self.module_list= create_yolov3_modules(anchors, anch_mask, n_classes, ignore_thre)
        self.length = len(self.module_list) 

    def forward(self, x, targets=None):
        """
        Forward path of YOLOv3.
        Args:
            x (torch.Tensor) : input data whose shape is :math:`(N, C, H, W)`, \
                where N, C are batchsize and num. of channels.
            targets (torch.Tensor) : label array whose shape is :math:`(N, 50, 5)`

        Returns:
            training:
                output (torch.Tensor): loss tensor for backpropagation.
            test:
                output (torch.Tensor): concatenated detection results.
        """
        train = targets is not None
        output = []
        route_layers = []
        for i in range(self.length):
            # yolo layers
            if i == 14 or i == 22 or i == 28:
                if train:
                    x, *loss_dict = self.module_list[i](x, targets)
                    #for name, loss in zip(['xy', 'wh', 'conf', 'cls', 'l2'] , loss_dict):
                    self.loss_list += loss_dict
                else:
                    x = self.module_list[i](x)
                output.append(x)
            else:
                x = self.module_list[i](x)

            # route layers
            if i == 6 or i == 8 or i == 12 or i == 20:
                route_layers.append(x)
            if i == 14:
                x = route_layers[2]
            if i == 22:  # yolo 2nd
                x = route_layers[3]
            if i == 16:
                x = torch.cat((x, route_layers[1]), 1)
            if i == 24:
                x = torch.cat((x, route_layers[0]), 1)

            i+=1
        if train:
            return sum(output)
        else:
            return torch.cat(output, 1)