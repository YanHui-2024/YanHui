import torch

def foo():
    current =  '''
        graph(%x : Float(20:10, 10:1)):
            return (%x)
    '''
    graph = torch._C.parse_ir(current)
    print(graph)

    desired =  '''
        graph(%x : Float(20, 10, strides=[10, 1])):
            return (%x)
    '''