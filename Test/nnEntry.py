import torch
import matplotlib.pyplot as plt
import torch.nn as nn
from torch.autograd import Variable
import numpy as np


n_data = torch.ones(100, 2)
x0 = torch.normal(2 * n_data, 1)  # 生成均值为2.标准差为1的随机数组成的矩阵 shape=(100, 2)
y0 = torch.zeros(100)
x1 = torch.normal(-2 * n_data, 1)  # 生成均值为-2.标准差为1的随机数组成的矩阵 shape=(100, 2)
y1 = torch.ones(100)

#合并数据x,y
x=torch.cat((x0,x1),0).type(torch.FloatTensor)
y=torch.cat((y0,y1),0).type(torch.FloatTensor)

print(x.data.numpy()[:,0])
#画图
# plt.scatter(x.data.numpy()[:,0],x.data.numpy()[:,1],c=y.data.numpy(),s=100,lw=0,cmap='RdYlGn')
# plt.show()

class LogisticRegression(nn.Module):
    def __init__(self):
        super(LogisticRegression,self).__init__()
        self.lr=nn.Linear(2,1)   #相当于通过线性变换y=x*T(A)+b可以得到对应的各个系数
        self.sm=nn.Sigmoid()   #相当于通过激活函数的变换

    def forward(self, x):
        x=self.lr(x)
        x=self.sm(x)
        return x

logistic_model=LogisticRegression()
if torch.cuda.is_available():#使用GPU
    logistic_model.cuda()


#定义损失函数和优化器
criterion=nn.BCELoss()   #选用BCE损失函数,该损失函数是只用于2分类问题的损失函数
optimizer=torch.optim.SGD(logistic_model.parameters(),lr=1e-3,momentum=0.9)  #采用随机梯度下降的方法

#开始训练
#训练10000次
for epoch in range(10000):
    if torch.cuda.is_available():
        x_data=Variable(x).cuda()
        y_data=Variable(y).cuda()
    else:
        x_data=Variable(x)
        y_data=Variable(y)

    out=logistic_model(x_data)  #根据逻辑回归模型拟合出的y值

    loss=criterion(out,y_data)  #计算损失函数
    print_loss=loss.data.item()  #得出损失函数值
    mask=out.ge(0.5).float()  #以0.5为阈值进行分类
    correct=(mask==y_data).sum()  #计算正确预测的样本个数
    acc=correct.item()/x_data.size(0)  #计算精度
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    #每隔20轮打印一下当前的误差和精度
    if (epoch+1)%20==0:
        print('*'*10)
        print('epoch {}'.format(epoch+1))  #误差
        print('loss is {:.4f}'.format(print_loss))
        print('acc is {:.4f}'.format(acc))  #精度


# 结果可视化
w0,w1=logistic_model.lr.weight[0]
w0=float(w0.item())
w1=float(w1.item())
b=float(logistic_model.lr.bias.item())
plot_x=np.arange(-7,7,0.1)
plot_y=(-w0*plot_x-b)/w1
plt.scatter(x.data.numpy()[:,0],x.data.numpy()[:,1],c=y.data.numpy(),s=100,lw=0,cmap='RdYlGn')
plt.plot(plot_x,plot_y)
plt.show()