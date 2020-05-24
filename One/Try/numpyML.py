import numpy as np
# dot:线代的矩阵相乘
s1 = [[1, 2, 3], [4, 5, 6]]
s2 = [[2, 2], [3, 3], [4, 4]]

# 跟线性代数计算矩阵一样，(1*15)*(15*1)=(1*1)
dot = np.dot(s1, s2)
print(dot)

nparray = np.array([[1, 2, 3, 4]])
# numpy转置
print(nparray.T)
print(np.dot(nparray, nparray.T))
# np的sigmoid


def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s




def Theta(preTheta, a, Xi, Yi):
    return preTheta+a*(Yi-sigmoid(np.dot(preTheta.T, Xi)))*Xi

print(sigmoid(np.dot(nparray, nparray.T)))
    # theta = theta+0.1*((Y[i])*torch.sigmoid(theta.t().mm(X[i]))*X[i])
print(nparray+[1, 2, 3, 4])
