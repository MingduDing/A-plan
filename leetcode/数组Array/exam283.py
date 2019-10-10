#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/6 15:55
# @Author:   Domi
# @File:     exam283.py
# @Software: PyCharm

"""
283.《移动零》（easy）

题目：给定一个数组nums，编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序

思路：双指针
"""
from copy import deepcopy


def move_zero_1(nums):
    """
    法1：快慢指针，i是快指针，j是慢指针
    :param nums:
    :return:
    """
    j = 0                                        # 初始化指针
    for i in range(len(nums)):                   # 循环遍历
        if nums[i] != 0:                         # 当前数不等于0时
            nums[j], nums[i] = nums[i], nums[j]  # 非0数往前移
            j += 1                               # j后移
    return nums                                  # 返回新数组


def move_zero_2(nums):
    """
    法2：内置函数方法remove和append
    :param nums:
    :return:
    """
    nums2 = deepcopy(nums)     # 深拷贝，对原数组的操作不影响新数组
    for num in nums:           # 循环遍历
        if num == 0:           # 判断
            nums2.remove(num)  # 移除0
            nums2.append(num)  # 添加0
    return nums2               # 最后输出


def move_zero_3(nums):
    """
    法3：统计0的个数，约束遍历范围，已经移动到末尾的0不需要再遍历，提高效率
    :param nums:
    :return:
    """
    i, count = 0, 0                   # 初始化指针和零的个数
    while i < len(nums)-count:        # 只要指针还在要查看的区域之内
        if nums[i] == 0:              # 如果遇到0
            nums.append(nums.pop(i))  # 弹出0加到数组末尾，pop和del是根据索引操作的，remove是根据数值操作
            count += 1                # 零的个数＋1
        else:                         # 否则
            i += 1                    # 指针＋1
    return nums                       # 返回结果


print(move_zero_3([0, 1, 0, 3, 0, 7, 0, 12]))
