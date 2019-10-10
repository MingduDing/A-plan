#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/6 15:10
# @Author:   Domi
# @File:     exam268.py
# @Software: PyCharm

"""
268.《缺失数字》（easy）

题目：给定一个包含0, 1, 2, ..., n中n个数的序列，找出0 ... n中没有出现在序列中的那个数

思路：数组，位运算
"""


def missing_number_1(nums):
    """
    法1：排序对比
    :param nums:
    :return:
    """
    nums.sort()                 # 将数组排序
    for i in range(len(nums)):  # 遍历数组
        if i != nums[i]:        # 如果遇到了断点
            return i            # 返回当前缺失值
    return len(nums)            # 缺失值是最大值


def missing_number_2(nums):
    """
    法2：集合相减
    :param nums:
    :return:
    """
    res = set(range(len(nums)+1)) - set(nums)
    return res.pop()


def missing_number_3(nums):
    """
    法3：求和相减
    :param nums:
    :return:
    """
    n = len(nums)
    return n*(n+1)//2 - sum(nums)


def missing_number_4(nums):
    """
    法4：异或
    :param nums:
    :return:
    """
    res = 0                     # 初始化一个结果变量，a^0==a
    for i in range(len(nums)):  # 遍历数组
        res ^= nums[i]          # 结果变量和元素中每个元素异或
        res ^= i                # 结果变量和预期数组的每个元素异或
    res ^= len(nums)            # 预期数组要多一个数，继续异或
    return res                  # 只出现一次的数就是结果


print(missing_number_2([0, 2, 1]))
