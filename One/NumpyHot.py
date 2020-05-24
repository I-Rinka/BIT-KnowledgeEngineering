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


def BuildIntoOneHotList(WordList, OneHotDic):
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


def ConvertListIntoDic(List):
    # 或许有减少冗余，加快运算的奇效
    dic = {}
    for l in List:
        if not l in dic:
            dic[l] = 0
    return dic


def GetYListFromOneHotList(XList, OneHotDic):
    """这里onehotdic指的是转化为向量后的dic"""
    Y = []
    for X in XList:
        if X in OneHotDic:
            Y.append(1)
        else:
            Y.append(0)
    return Y


def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s


def Theta(preTheta, a, Xi, Yi):
    return preTheta+a*(Yi-sigmoid(np.dot(preTheta.T, Xi)))*Xi


# OHLst = BuildIntoOneHotList(p1.entityWord, p1.oneHotDic)
# OHD = ConvertListIntoDic(OHLst)

p1 = FR.OneHotBuilder(R'data/1998-01-2003版-带音.txt', "19980101", "19980120")
X = BuildIntoOneHotList(p1.linkedWord, p1.oneHotDic)
cutOff = 50
l = len(p1.oneHotDic)
theta = np.zeros([l, 1], dtype=np.float)
Y = GetYListFromOneHotList(p1.linkedWord, p1.entityWord)
veri = FR.OneHotBuilder(R'data/1998-01-2003版-带音.txt', "19980101", "19980120")

X2 = BuildIntoOneHotList(veri.linkedWord, p1.oneHotDic)
# Y2 = np.zeros([l, 1], dtype=np.float)
pltX = []
pltY = []
YV = GetYListFromOneHotList(veri.linkedWord, p1.entityWord)
for i in range(cutOff):
    pltX.append(i)
    ytu = 0
    for Xi in X:
        # j = random.randint(0, len(X)-1)
        theta = Theta(theta, 0.05, Xi, Y[ytu])
        ytu += 1
    accu = 0
    num = 0
    itu = 0
    for xi in X2:
        yi = sigmoid(np.dot(theta.T, xi))
        if yi >= 0.5:
            num += 1
            if YV[itu] == 1:
                accu += 1
        itu += 1
    accurate = accu/num
    complete = accu/len(veri.entityWord)
    F1 = 2*accurate*complete/(accurate+complete)
    # y2 = torch.sigmoid(theta.t().mm(xe))解码
    print(F1)
    # print(theta)

    pltY.append(F1)

plt.plot(pltX, pltY)
plt.savefig("test.png", dpi=220)
plt.show()
