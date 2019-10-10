#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/12 10:40
# @Author : Domi
# @File : exam004.py
# @Software: PyCharm

"""
1.《两数之和》（easy）

题目：给定一个整数数组nums和一个目标值target，请你在该
数组中找出和为目标值的那两个整数，并返回他们的数组下标。

思路：使用enumerate(sequence,index)函数，参数index可
以确定起始索引，函数返回一个元组(index,value).
"""


def two_sum(nums, target):
    """
    1.两数之和
    :param nums: 整数数组
    :param target: 目标值
    :return: d[target-num], i
    """
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            print(d[target-num], i)  # d[target-num]是前面一个数的索引，i是后面数的索引
        d[num] = i  # num是key, i是value


two_sum([20, 2, 6, 11, 15, 9, 7], 9)
