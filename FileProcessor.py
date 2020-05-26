#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   FileReader.py
@Time    :   2020/05/25 10:29:06
@Author  :   Rinka
@Contact :   I_Rinka@outlook.com
@License :   (C)Copyright 2019-2020, BIT_Rinka
@Desc    :   None
'''


# here put the import lib


def file_read(path):
    file = open(path, "r", encoding="utf-8")
    result = []
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        result.append(line)
    file.close()
    return result


def file_read_section(path, start_flag, end_flag):
    """
    给定起始、结束区间的标记，读入指定区间的行
    """
    file = open(path, "r", encoding="utf-8")
    result = []
    switch1 = False
    switch2 = False
    while True:
        line = file.readline()
        if switch1 == False and line.startswith(start_flag):
            switch1 = True
        if line.startswith(end_flag):
            switch2 = True
        elif switch2:
            break
        if switch1:
            line.strip()
            result.append(line)
    lines = file.readlines()
    file.close()
    return result


def file_write(path, content_string):
    '''
    写入内容只能接受字符串
    方法是在源文件结尾处追加
    '''
    file = open(path, "a+", encoding="utf-8")
    file.write(content_string)
    file.close()


def file_write_cover(path, content_string):
    '''
    写入内容只能接受字符串
    方法是覆盖源文件
    '''
    file = open(path, "a+", encoding="utf-8")
    file.write(content_string)
    file.close()


def code_convert(input_path, input_code, output_code="utf-8", output_path="./convert_out.txt"):
    '''
    转换字符集编码，比如输入gbk，输出utf8
    '''
    file = open(input_path, "r", encoding=input_code)
    result = []
    lines = file.readlines()
    for line in lines:
        result.append(line)
    file.close()
    file = open(output_path, "w+", encoding=output_code)
    for line in result:
        file.write(line)
    file.close()
