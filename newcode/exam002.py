#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/5 17:06
# @Author:   Domi
# @File:     exam004.py
# @Software: PyCharm

"""
《大整数相乘》

题目：有两个用字符串表示的非常大的大整数,算出他们的乘积，也是
用字符串表示。不能用系统自带的大整数类型

思路：数学乘法，先乘后加，需要注意两个数的循环条件和顺序
"""

s1, s2 = input().split()
ret = [0]*(len(s2)+len(s1))  # 创建指定大小的全0数组
# ret = [[0] for _ in range(len(s2)+len(s1))]
for x in range(len(s2)):
    for y in range(len(s1)):
        ret[x+y+1] += int(s2[x])*int(s1[y])
for i in range(len(ret)-1, 0, -1):
    ret[i-1] += ret[i]//10  # 进位
    ret[i] %= 10  # 取模
if ret[0] == 0:
    del ret[0]
print(''.join(map(str, ret)))
