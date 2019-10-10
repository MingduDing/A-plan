#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/12 14:40
# @Author:   Domi
# @File:     exam240.py
# @Software: PyCharm

"""
240.《搜索二维矩阵II》（medium）

题目：编写一个高效的算法来搜索mxn矩阵matrix中的一个目标值target。该矩阵具有以下特性：
每行的元素从左到右升序排列
每列的元素从上到下升序排列

思路：分治算法，二分查找
"""


def search_matrix(matrix, target):
    m = len(matrix)                      # matrix的"行数"，第一个维度
    n = len(matrix[0])                   # matrix的"列数"，第二个维度
    if not matrix or m == 0 or n == 0:   # 如果矩阵为空
        return False                     # 返回假
    row = 0                              # 行索引
    col = n-1                            # 列索引
    while row < m and col >= 0:          # 满足条件时进入循环
        if target == matrix[row][col]:   # 如果目标值存在
            return True                  # 直接返回真
        elif target < matrix[row][col]:  # 如果目标值小于当前值
            col -= 1                     # 列索引减1
        else:                            # 否则
            row += 1                     # 行索引加1
    return False                         # 返回假


# nums = [[]]
nums = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
print(search_matrix(nums, 14))
