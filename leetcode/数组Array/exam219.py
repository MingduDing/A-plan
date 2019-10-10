#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/6 14:43
# @Author:   Domi
# @File:     exam219.py
# @Software: PyCharm

"""
219.《存在重复元素II》（easy）

题目：给定一个整数数组和一个整数k，判断数组中是否存在两个不同的索引i
和j，使得nums[i]=nums[j]，并且i和j的差的绝对值最大为k

思路：哈希表
"""


def contains_duplicate(nums, k):
    """
    :param nums:
    :param k:
    :return:
    """
    if len(nums) <= 1:
        return False

    d = {}
    # for num in nums:
    #     if num in d and ......  这里的循环条件必须要写成i的形式，因为需要用到索引
    for i in range(len(nums)):  # 遍历数组
        if nums[i] in d and i-d[nums[i]] <= k:  # 如果当前数字出现过并且之前出现的位置与当前位置差小于阈值k
            return True
        d[nums[i]] = i   # 没有出现过或者出现位置离当前太远，则加入或更新当前元素及其位置到字典中
    return False


print(contains_duplicate([1, 2, 3, 1], 3))

