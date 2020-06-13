import torch
x=torch.zeros(3)
x[1]=2
x[2]=1
print(x)
print(x.view(len(x),-1))