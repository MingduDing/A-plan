#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/12 10:43
# @Author : Domi
# @File : exam026.py
# @Software: PyCharm

"""
26.删除排序数组中的重复项（easy）

题目：给定一个排序数组，你需要在原地删除重复出现的元素，使
得每个元素只出现一次，返回移除后数组的新长度。不要使用额外
的空间，必须在原地修改并只使用O(1)的额外空间。

思路：数组是有序的，使用快慢指针，慢指针i自加1，快指针j放
在for循环中，遍历数组，判断前后值是否相等，相等时j后移，
不相等时i加1，值交换
"""


def remove_duplicates(nums):
    """
    26.删除排序数组中的重复项
    :param nums: 排序数组
    :return: num[:i+1]
    """
    n = len(nums)
    i = 0
    if n == 0:
        return None
    for j in range(1, n):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    print(nums[:i+1], '总数是:', i+1)


remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 3])
