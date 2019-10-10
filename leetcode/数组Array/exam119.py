#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/16 22:50
# @Author : Domi
# @File : exam119.py
# @Software: PyCharm

"""
119.杨辉三角II（easy）

题目：给定一个非负索引k，k<=33, 返回杨辉三角的第k行。

思路：动态规划。首先生成需要维度大小的全1数组，外层循环遍
历对应行，内层循环对应列，例如a=[[1],[2,3],[4,5,6]],则
a[1][1]=3。返回当前行的索引是row_index。

对比：和118比较，这里的row_index是索引值，是真实列数加1
"""


def get_row(row_index):
    """
    118:杨辉三角II
    :param row_index: 非负索引
    :return: ans[row_index-1]
    """
    ans = [[1]*n for n in range(1, row_index+2)]  # 生成需要大小的全1数组
    for i in range(3, row_index+2):
        for j in range(0, i-2):
            ans[i-1][j+1] = ans[i-2][j] + ans[i-2][j+1]

    print(ans[row_index])


num = 3
get_row(num)
