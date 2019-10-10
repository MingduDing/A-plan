#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/6 10:17
# @Author:   Domi
# @File:     exam167.py
# @Software: PyCharm

"""
167.《两数之和II》（easy）

题目：给定一个已按照升序排列的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值index1和index2，其中index1必须小于index2，返回的下
标值（index1 和 index2）不是从零开始的

思路：二分查找，双指针，数组
"""


def two_sum(nums, target):
    start, end = 0, len(nums)-1
    while start < end:
        res = nums[start] + nums[end]
        if res > target:
            end -= 1
        elif res < target:
            start += 1
        else:
            return start+1, end+1


print(two_sum([2, 6, 7, 9, 11, 15, 20], 9))
