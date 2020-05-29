import torch.nn as nn
import torch

'''
class SoftMaxModel(nn.Module):
    def __init__(self):
        super(SoftMaxModel, self).__init__()
        self.lr = nn.Linear(5, 3)  # 相当于通过线性变换y=x*T(A)+b可以得到对应的各个系数，里面是内置了θ！？

    def forward(self, x):
        x = self.lr(x)
        return x


x = torch.randn([4, 5])
net = SoftMaxModel()

print(net.lr.weight)

print(net(x))

optimizer = torch.optim.SGD(net.parameters(), lr=0.2)

prediction = net(x)     # 喂给 net 训练数据 x, 输出预测值

loss_func=torch.nn.CrossEntropyLoss()

loss = loss_func(prediction, torch.tensor([0,1,2,1]))     # 计算两者的误差

optimizer.zero_grad()   # 清空上一步的残余更新参数值
loss.backward()         # 误差反向传播, 计算参数更新值
optimizer.step()        # 将参数更新值施加到 net 的 parameters 上

print(net(x))

print(net.lr.weight)

'''

# inp=torch.randn([4,3])
# print(inp)
# target=torch.tensor([0,1,2,1])#这输入的是标签
# loss=torch.nn.CrossEntropyLoss()
# print(loss(inp,target))

# class MultiClassify(torch.nn.Module):
#     def __init__(self):
#         super(MultiClassify, self).__init__()
#         self.theta = torch.nn.Linear(150, 3)

#     def forward(self, x):
#         x-self.theta(x)
#         return x

# net=MultiClassify()
# x=torch.randn([150,100])
# # net(x)
# # print(x)
# # print(x[0])
# x2=torch.randn(150)
# print(net(x2))
# x=torch.randn(3,150)
# print(x)
# print(m(x))

m=nn.Linear(150,3)
x=torch.randn(150)
x=x.unsqueeze(0)
x2=torch.randn(150)
x3=torch.cat((x,x2.unsqueeze(0)))
print(x3)
print(m(x3))
# x2=torch.randn(2,150)
# print(m(x2))