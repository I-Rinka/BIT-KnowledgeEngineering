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
print(theta)
# 到时候应该改为random
for i in range(len(X)):
    theta=theta+0.01*((Y[i])*torch.sigmoid(theta.t().mm(X[i]))*X[i])
    print(theta)

# theta相当于是逆向的，接下来要搞正向的
# print(Y[0:10000])
