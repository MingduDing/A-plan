#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/9 11:07
# @Author:   Domi
# @File:     exam566.py
# @Software: PyCharm

"""
566.《重塑矩阵》（easy）

题目：在MATLAB中，有一个非常有用的函数reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。
给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。重构后的矩阵需要将原始矩
阵的所有元素以相同的行遍历顺序填充。如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出
原始矩阵

思路：二维数组的遍历方法
"""


def matrix_reshape(nums, r, c):
    m = len(nums)                             # nums的"行数"，第一个维度
    n = len(nums[0])                          # nums的"列数"，第二个维度
    if r*c != m*n:                            # 如果维度不同
        return nums                           # 则返回原矩阵
    tmp = [[0]*c for _ in range(r)]           # c=2, r=4. [[0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(r*c):                      # 循环遍历，i: 0, 1, 2, 3, 4, 5, 6, 7
        tmp[i//c][i % c] = nums[i//n][i % n]  # i//c求第一个维度，i%c求第二个维度
    return tmp                                # 返回变形之后的矩阵[[1, 2], [3, 4], [5, 6], [7, 8]]


print(matrix_reshape([[1, 2, 3, 4], [5, 6, 7, 8]], 4, 2))
