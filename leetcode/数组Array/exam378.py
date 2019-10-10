#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/12 16:31
# @Author:   Domi
# @File:     exam378.py
# @Software: PyCharm

"""
378.《有序矩阵中第K小的元素》（medium）

题目：给定一个nxn矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第k小元素，而不是第k个元素

思路：二分查找
"""
import heapq


def kth_smallest_1(matrix, k):
    """
    法1：矩阵展开为一维数组，排序
    :param matrix:
    :param k:
    :return:
    """
    n = len(matrix)
    alist = []
    for i in range(n):
        for j in range(n):
            alist.append(matrix[j][i])
    alist.sort()
    return alist[k-1]


def kth_smallest_2(matrix, k):
    """
    法2：堆
    :param matrix:
    :param k:
    :return:
    """
    visited = {(0, 0)}
    heap = [(matrix[0][0], (0, 0))]
    while heap:
        val, (i, j) = heapq.heappop(heap)
        k -= 1
        if k == 0:
            return val
        if i+1 < len(matrix) and (i+1, j) not in visited:
            heapq.heappush(heap, (matrix[i+1][j], (i+1, j)))
            visited.add((i+1, j))
        if j+1 < len(matrix) and (i, j+1) not in visited:
            heapq.heappush(heap, (matrix[i][j+1], (i, j+1)))
            visited.add((i, j+1))


nums = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
print(kth_smallest_2(nums, 8))
