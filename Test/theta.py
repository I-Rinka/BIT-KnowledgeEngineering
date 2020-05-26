import torch
theata=torch.randn(2,10)
print(theata)
theata[0]*=torch.zeros(10)
print(theata)