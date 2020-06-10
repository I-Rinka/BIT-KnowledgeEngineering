import torch
bed = torch.zeros(20, 10)  # 高/长
one = torch.ones(10)
bed[0] += one
print(bed)
