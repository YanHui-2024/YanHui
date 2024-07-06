import torch
test =  '''
    graph(%x : Float(20, *)):
        return (%x)
'''
graph = torch._C.parse_ir(test)