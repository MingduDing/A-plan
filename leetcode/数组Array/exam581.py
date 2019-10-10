#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/9 15:42
# @Author:   Domi
# @File:     exam581.py
# @Software: PyCharm

"""
581.《最短无序连续子数组》（easy）

题目：给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
你找到的子数组应是最短的，请输出它的长度

思路：左右指针
"""


def find_unsorted_array(nums):
    sorted_num = sorted(nums)                 # 排序
    if sorted_num == nums:                    # 如果输入有序
        return 0                              # 返回0

    left = 0                                  # 初始化左指针
    while True:                               # 当为真时进入循环
        if nums[left] != sorted_num[left]:    # 遇到第一个不同元素
            break                             # 退出循环
        left += 1                             # 左指针右移

    right = len(nums) - 1                     # 初始化右指针
    while True:                               # 当为真时进入循环
        if nums[right] != sorted_num[right]:  # 遇到第一个不同元素
            break                             # 跳出循环
        right -= 1                            # 右指针左移

    return right - left + 1                   # 返回需要跳针的字串长度


def find_unsorted_array_simple(nums):
    # 记录下原数组和排序后数组相应元素不同的所有位置，并组成列表
    diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
    # 如果有不同元素，返回不同元素的最右端位置和最左端位置之差，否则返回零
    return len(diff) and max(diff) - min(diff) + 1  # 成立的话返回左边的数


print(find_unsorted_array_simple([2, 6, 4, 8, 10, 9, 15]))
