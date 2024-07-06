'''
This following load of torchscript model does not enforce parameters 
to be mapped to a CPU when it is originally mapped to a GPU
'''
torch.load('<torchscript-file-path>', map_location=torch.device('cpu')) # fails when no GPU is available