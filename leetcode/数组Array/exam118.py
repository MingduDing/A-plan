#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/16 16:23
# @Author : Domi
# @File : exam118.py
# @Software: PyCharm

"""
118.杨辉三角（easy）

题目：给定一个非负整数numRows，生成杨辉三角的前numRows行。

思路：动态规划。首先生成需要维度大小的全1数组，外层循环遍
历对应行，内层循环对应列，例如a=[[1],[2,3],[4,5,6]],则
a[1][1]=3。
"""


def generate(num_rows):
    """
    118:杨辉三角
    :param num_rows: 非负整数
    :return: ans
    """
    ans = [[1]*n for n in range(1, num_rows+1)]  # 生成需要大小的全1数组
    for i in range(3, num_rows+1):
        for j in range(0, i-2):
            ans[i-1][j+1] = ans[i-2][j] + ans[i-2][j+1]

    print(ans)


num = 5
generate(num)
