#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/16 14:25
# @Author : Domi
# @File : exam088.py
# @Software: PyCharm

"""
88.合并两个有序数组（easy）

题目：给定两个有序整数数组nums1和nums2，将nums2合并到nums1中，
使得nums1成为一个有序数组。

思路：双指针。将指针p1置为nums1的末尾，p2为nums2的末尾，在每一
步将最小值放入输出数组中。
"""


def merge(nums1, m, nums2, n):
    """
    88.合并两个有序数组
    :param nums1: 有序整数数组1
    :param m:     num1元素数量
    :param nums2: 有序整数数组2
    :param n:     num2元素数量
    :return:      合并后的nums1
    """

    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1

    nums1[:p2+1] = nums2[:p2+1]  # 防止nums2中遗漏元素

    print(nums1)


nums1_1 = [5, 6, 7, 0, 0, 0]
nums2_2 = [1, 2, 3]
merge(nums1_1, 3, nums2_2, 3)
