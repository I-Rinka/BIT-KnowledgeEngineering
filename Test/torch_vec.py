import torch
a=torch.ones(10)
for i in range(len(a)):
    a[i]=0.1
print(a*a)