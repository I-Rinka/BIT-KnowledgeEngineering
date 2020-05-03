#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tensorProcessor.py
@Time    :   2020/05/02 16:09:11
@Author  :   Rinka
@Contact :   I_Rinka@outlook.com
@License :   (C)Copyright 2019-2020, BIT_Rinka
@Desc    :   None
'''

# here put the import lib
# 建立接受数字就可以得到许多向量元组
# import FileReader as FR
import matplotlib.pyplot as plt
import random
import FileReader as FR
import numpy as np
import torch
if torch.cuda.is_available():
    device = torch.device("cuda")
# 把词语表通过OneHot转换为特征向量
# 输入：一维词表，定义好了的向量词典


def ConvertWordsToTensor(words, dic):
    l = len(dic)
    z = np.zeros([l, 1], dtype=np.float)
    for w in words:
        if w in dic:
            z[dic[w]] = 1
        else:
            z[dic['UNKNOWN']] = 1
    return z


fr = FR.OneHotBuilder(R'data/1998-01-2003版-带音.txt', "19980101", "19980120")

# 把y[i]建成一个numpy向量列表？

X = []
for w in fr.linkedWord:
    z = ConvertWordsToTensor(w, fr.oneHotDic)
    X.append(torch.from_numpy(z))

Y = []
for w in fr.linkedWord:
    if w in fr.entityWord:
        # Y.append(1)
        Y.append(torch.tensor([1.]))
    else:
        # Y.append(0)
        Y.append(torch.tensor([0.]))

theta = torch.rand_like(X[1])
# print(theta)
# # 到时候应该改为random
# for i in range(len(X)):
#     theta = theta+0.01*((Y[i])*torch.sigmoid(theta.t().mm(X[i]))*X[i])
#     print(theta)

# theta相当于是逆向的，接下来要搞正向的
# print(Y[0:10000])
# 正向：
veri = FR.OneHotBuilder(R'data/1998-01-2003版-带音.txt', "19980121", "19980125")
X2 = []
for w in veri.linkedWord:
    z = ConvertWordsToTensor(w, fr.oneHotDic)
    X2.append(torch.from_numpy(z))

# Y2[i] = torch.sigmoid(theta.t().mm(X2[i]))

cutOff = 100
p5 = torch.tensor([0.5])


pltX = []
pltY = []

# 最好建立一个entitiyWord的词典
for j in range(cutOff):
    i = random.randint(0, len(Y))
    theta = theta+0.01*((Y[i])*torch.sigmoid(theta.t().mm(X[i]))*X[i])
    i2 = 0
    a = 0
    b = 0
    # EntityWord以后要放到字典，这里还有重大bug
    c = len(fr.entityWord)
    for xe in X2:
        y2 = torch.sigmoid(theta.t().mm(xe))
        i2 += 1
        if y2 >= p5:
            b += 1
            if veri.linkedWord[i2] in fr.entityWord:
                a += 1
    accurate = a/b
    complete = a/c
    F1 = 2*accurate*complete/(accurate+complete)
    pltX.append(j)
    pltY.append(F1)

plt.plot(pltX, pltY)
plt.savefig("test.png", dpi=220)
plt.show()
