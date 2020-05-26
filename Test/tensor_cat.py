import torch
# a=torch.ones(50)
# b=torch.zeros(50)
a=torch.tensor([[50]])
b=torch.tensor([[100]])
c=torch.cat([a,b],dim=0)
print(c)