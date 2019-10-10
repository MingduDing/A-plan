#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/9/16 9:34
# @Author:   Domi
# @File:     动脑子认老乡.py
# @Software: PyCharm

"""
输入
包含多组测试用例。
对于每组测试用例：
第一行包括2个整数，N（1 <= N <= 1000），M(0 <= M <= N*(N-1)/2)，代表现有N个人（用1~N编号）和M组关系；
在接下来的M行里，每行包括3个整数，a，b, c，如果c为1，则代表a跟b是同乡；如果c为0，则代表a跟b不是同乡；
已知1表示小赛本人。

输出
对于每组测试实例，输出一个整数，代表确定是小赛同乡的人数。

样例输入     样例输出
3 1         0
2 3 1       3
5 4
1 2 1
3 4 0
2 5 1
3 2 1

时间限制
C/C++语言：1000000MS其它语言：1002000MS
内存限制
C/C++语言：67108864KB其它语言：67633152KB
"""

import math
while True:
    # 每组第一行是N和M
    nm = list(map(int, input().split()))
    N = nm[0]
    M = nm[1]
    print(str(N) + ' ' + str(M))
    # 接下来M行，每行a b c
    for i in range(M):
        abc = list(map(int, input().split()))
        a = abc[0]
        b = abc[1]
        c = abc[2]
        print(str(a) + ' ' + str(b) + ' ' + str(c))
