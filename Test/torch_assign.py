import torch
x = torch.zeros(20)
x[1] = 1  # pytorch可以直接这么赋值
print(x)
x2 = torch.ones(20)
xn = torch.cat([x, x2]).cuda()
print(xn)
# print(torch.sum(x2)).cuda?
