import torch

y=torch.randn(3)
print(y)
print(y.max(0))
# print(y.max(1))
print(torch.tensor([0,0,1])==torch.tensor([0,0,1]))
if (torch.tensor([0,0,1])==torch.tensor([0,0,1]))[0]:
    print("wow")

o=torch.tensor([0,0,1])
if o[2]==1:
    print("zero")
if o[2]==0:
    print("not zero")