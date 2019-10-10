#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/9/18 14:03
# @Author:   Domi
# @File:     约德尔测试.py
# @Software: PyCharm

"""
输入
每组输入数据为两行，第一行为有关约德尔人历史的字符串，第二行是黑默丁格观测星空得到的字符串。
(两个字符串的长度相等,字符串长度不小于1且不超过1000。)

样例输入
@!%12dgsa
010111100

输出
输出一行，在这一行输出相似率。用百分数表示。(相似率为相同字符的个数/总个数,精确到百分号小数点后两位。print("%%");输出一个%。)

样例输出
66.67%
"""

ch = input()
x = []
count = 0
for i in ch:
    if i.isdigit() is True or i.isalpha() is True:
        x.append('1')
    else:
        x.append('0')
num = list(input())
for i, j in zip(num, x):
    if i == j:
        count += 1
print("%.2f%%" % (count / len(ch) * 100))
