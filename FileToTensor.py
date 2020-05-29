#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   FileToTensor.py
@Time    :   2020/05/27 23:37:41
@Author  :   Rinka 
@Contact :   I_Rinka@outlook.com
@License :   (C)Copyright 2019-2020, BIT_Rinka
@Desc    :   None
'''

# here put the import lib

import random
import FileProcessor as FP
import VectorGet as VG
import torch
import matplotlib.pyplot as plt


def LineProcessor(line):
    spt = line.split('  ')
    BIO_line = []
    BIO_switch1 = False
    if len(spt) >= 1:
        if spt and spt[0]:
            for w in spt:
                if 'm' not in w and 'w' not in w:  # 过滤掉所有符号
                    if w[0] == '[':
                        BIO_line.append([w[1:w.find('/')], 0])
                        BIO_switch1 = True
                    else:
                        if BIO_switch1 == True:
                            BIO_line.append([w[0:w.find('/')], 1])
                            if ']' in w:
                                BIO_switch1 = False
                        else:
                            BIO_line.append([w[0:w.find('/')], 2])
    return BIO_line


def GetBIOSet(data_set):
    BIO_SET = []
    for line in data_set:
        bio_line = LineProcessor(line)  # 得到词和对应的BIO标签
        if bio_line:
            BIO_SET.append(bio_line)
    return BIO_SET


def BIOSetToTensorXY(BIO_SET, VE):
    '''
    将词和对应的BIO分类都转换为向量
    每一个元素的第一项为X的向量(同时拼接了前中后词)
    第二项为Y的向量    
    '''
    X_Y_Tensor = []
    for bio_line in BIO_SET:
        for i in range(len(bio_line)):
            if i == 0:
                preWord = VE.GetWordVector("Unknow")
            else:
                preWord = VE.GetWordVector(bio_line[i-1][0])
            if i == len(bio_line)-1:
                aftherWord = VE.GetWordVector("Unknow")
            else:
                aftherWord = VE.GetWordVector(bio_line[i+1][0])
            nowWord = VE.GetWordVector(bio_line[i][0])
            vec = torch.cat([preWord[0], nowWord[0], aftherWord[0]])
            X_Y_Tensor.append([vec, bio_line[i][1]])
    return X_Y_Tensor


def TransFileIntoTensor(file_path, vector_essential):
    '''
    唯一对外开放的函数
    输入文件位置后，得到对应的词向量和对应分类的元组列表
    '''
    data = FP.file_read(file_path)
    BIO_set = GetBIOSet(data)
    XY_Tensor = BIOSetToTensorXY(BIO_set, vector_essential)
    return XY_Tensor  # 这是一大坨集合
