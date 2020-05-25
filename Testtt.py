#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   vectorInput.py
@Time    :   2020/05/25 00:15:43
@Author  :   Rinka 
@Contact :   I_Rinka@outlook.com
@License :   (C)Copyright 2019-2020, BIT_Rinka
@Desc    :   None
'''
import Util.FileProcessor as FR
# here put the import lib
vector_file_path = 'Two\data\ctb.50d.vec'
# f = open(vector_file_path, "r", encoding='UTF-8')
# for i in range(1):
#     line = f.readline()
#     vec = line.split(' ')
#     for j in range(len(vec)):
#         if j!=0 and j!=len(vec)-1:
#             print(j-1, end=' ')
#             print(float(vec[j]))

rs = FR.file_read(vector_file_path)  # 读过的东西会被自动去除结尾\n
out = "out.txt"
FR.file_write_cover(out, "\n")
for r in range(40):
    pass
    FR.file_write("out.txt", rs[r]+"\n")

test_path = "Two\\data\\1998-01-2003版-带音.txt"
rs2 = FR.file_read_section(test_path, "19980101", "19980120")

for r in range(40):
    pass
    FR.file_write("out2.txt", rs2[r]+"\n")


def GetWord(line):
    """输入：文件读入的一行字符串|返回值：二维列表，二维列表的第二个属性为词性"""
    # line = self.__f.readline()
    splt = line.split('  ')
    out = []
    for v in splt:
        if v[0] == '[':
            out.append([v[1:v.find('/')], v[v.find('/'):]])
        else:
            out.append([v[0:v.find('/')], v[v.find('/'):]])
        # out.append([v[0:v.find('/')], v[v.find('/'):]])
    return out
