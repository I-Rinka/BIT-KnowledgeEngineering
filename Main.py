#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Main.py
@Time    :   2020/05/01 19:23:56
@Author  :   Rinka 
@Contact :   I_Rinka@outlook.com
@License :   (C)Copyright 2019-2020, BIT_Rinka
@Desc    :   None
'''

# here put the import lib
import FileReader as FR
p=FR.OneHotBuilder(R'C:\Users\I_Rin\Documents\Dev\KnowledgeEn\One\data/1998-01-2003版-带音.txt', "19980101", "19980120")
print(p.GetDemension("中国"))