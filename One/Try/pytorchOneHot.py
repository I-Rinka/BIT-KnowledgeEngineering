#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pytorchOneHot.py
@Time    :   2020/05/06 09:56:40
@Author  :   Rinka 
@Contact :   I_Rinka@outlook.com
@License :   (C)Copyright 2019-2020, BIT_Rinka
@Desc    :   None
'''

# here put the import lib
import torch
class_num = 10
batch_size = 4
label = torch.LongTensor(batch_size, 1).random_() % class_num
one_hot = torch.zeros(batch_size, class_num).scatter_(1, label, 1)
print(one_hot)
label