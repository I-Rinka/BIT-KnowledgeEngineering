import torch

if (torch.tensor([0,0,1]).max(0)==torch.tensor([0,0,0.1]).max(0)):
    print("wow")
