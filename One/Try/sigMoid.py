import torch
if torch.cuda.is_available():
    device = torch.device("cuda")          # a CUDA device object
    # y = torch.ones_like(x, device=device)  # 直接在GPU上创建tensor
    # x = x.to(device)                       # 或者使用`.to("cuda")`方法
    # z = x + y
    # print(z)
    # print(z.to("cpu", torch.double))
# a=torch.randn(10,1)
# # a=torch.zeros([10,1])
# b=torch.sigmoid(a)
# print(a)
# print(b)
a = torch.tensor([5.],device=device)  # 一定要带点
b=torch.ones([300000000,2],device=device)*a
# a = torch.tensor([5.])  # 一定要带点
# b=torch.ones([300000000,2])*a
print(b)
print(b*5)
# c=torch.rand_like(b)
# for i in range(10):
#     print(b.t().mm(c))
# bt=torch.transpose(b,0,1)
# print(b.mm(bt))
# c=torch.rand_like(b)
# c=torch.transpose(c)
# # print(b.mul(a))
# print(torch.sigmoid(b))

# a=torch.tensor([[1.],[2.]])
# print(a)
# b=torch.transpose(a,0,1)#矩阵转置要指定维度
# print(b)