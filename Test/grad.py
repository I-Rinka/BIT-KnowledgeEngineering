import torch
a = torch.tensor([[1],[2],[3.],[4]])    # 4*1列向量
X = torch.tensor([[1,2,3],[5,6,7],[8,9,10],[5,4,3.]],requires_grad=True)  #4*3矩阵，注意，值必须要是float类型
b = torch.tensor([[2],[3],[4.]]) #3*1列向量
f = a.view(1,-1).mm(X).mm(b)  # f = a^T.dot(X).dot(b)
f.backward()
print(f)
print(X.grad)   #df/dX = a.dot(b^T)
a.grad 
b.grad   # a和b的requires_grad都为默认(默认为False)，所以求导时，没有梯度
print(a.mm(b.view(1,-1)))  # a.dot(b^T)

f2=a.t()@X@b
print(f2)
f2.backward()
print(X.grad)