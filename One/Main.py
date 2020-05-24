#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   NumpyHot.py
@Time    :   2020/05/06 13:07:50
@Author  :   Rinka
@Contact :   I_Rinka@outlook.com
@License :   (C)Copyright 2019-2020, BIT_Rinka
@Desc    :   None
'''

# here put the import lib
import matplotlib.pyplot as plt
import random
import numpy as np
import FileReader as FR


def GetXListFromOneHotList(WordList, OneHotDic):
    # input|output
    l = len(OneHotDic)
    List = []
    for WL in WordList:
        z = np.zeros([l, 1], dtype=np.float)
        for word in WL:
            if word in OneHotDic:
                z[OneHotDic[word]] = 1
            else:
                z[OneHotDic['UNKNOWN']] = 1
        List.append(z)
    return List


def GetYListFromOneHotList(XList, OneHotDic):
    Y = []
    for X in XList:
        if X in OneHotDic:
            Y.append(1)
        else:
            Y.append(0)
    return Y


def Sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s


def Theta(preTheta, a, Xi, Yi):
    return preTheta+a*(Yi-Sigmoid(np.dot(preTheta.T, Xi)))*Xi


# 输入训练集和验证集
trainer = FR.OneHotBuilder(
    R'data/1998-01-2003版-带音.txt', "19980101", "19980120")
veri = FR.OneHotBuilder(R'data/1998-01-2003版-带音.txt', "19980121", "19980125")

# 构造Onehot向量
X = GetXListFromOneHotList(trainer.linkedWord, trainer.oneHotDic)
Y = GetYListFromOneHotList(trainer.linkedWord, trainer.entityWord)
XV = GetXListFromOneHotList(veri.linkedWord, trainer.oneHotDic)
YV = GetYListFromOneHotList(veri.linkedWord, trainer.entityWord)
l = len(trainer.oneHotDic)


pltX = []
pltY = []
# 初始化θ
theta = np.zeros([l, 1], dtype=np.float)
# 迭代次数
cutOff = 500
for turn in range(cutOff):
    pltX.append(turn)
    yi = 0
    # 使用全梯度下降
    for Xi in X:
        theta = Theta(theta, 0.01, Xi, Y[yi])
        yi += 1
    accu = 0
    num = 0
    i = 0
    for xi in XV:
        yi = Sigmoid(np.dot(theta.T, xi))
        # 判断是否预测准确
        if yi >= 0.5:
            num += 1
            if YV[i] == 1:
                accu += 1
        i += 1
    accurate = accu/num
    complete = accu/len(veri.entityWord)
    F1 = 2*accurate*complete/(accurate+complete)
    print("轮数：")
    print(turn)
    print("F1:%f 查准率：%f 查全率：%f" % (F1,accurate, complete))
    print("------------")
    pltY.append(F1)

plt.plot(pltX, pltY)
plt.savefig("test.png", dpi=220)
plt.show()
