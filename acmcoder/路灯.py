#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/9/18 14:04
# @Author:   Domi
# @File:     路灯.py
# @Software: PyCharm

"""
输入
输入两行数据，第一行是两个整数：路灯数目n (1≤n≤1000)，街道长度l (1≤l≤109)。
第二行有n个整数ai (0≤ai≤l)，表示路灯坐标，多个路灯可以在同一个点，也可以安放在终点位置。

样例输入
7 15
15 5 3 7 9 14 0

输出
输出能够照亮整个街道的最小d，保留两位小数。

样例输出
2.50
"""

num, n = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))
# arr = [int(i) for i in input().split()]
a = sorted(arr)
dist = []
for i in range(num - 1):
    dst = a[i+1] - a[i]
    dist.append(dst/2)
dist.append(a[0])
dist.append(n - a[-1])
d = sorted(dist)[-1]
print('%.2f' % d)
