#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/15 17:02
# @Author:   Domi
# @File:     exam004.py
# @Software: PyCharm

"""
004.《寻找两个有序数组的中位数》（easy）

题目：给定两个大小为m和n的有序数组nums1和nums2。请你找出这两个有序数组的中位数，
并且要求算法的时间复杂度为O(log(m+n))。可以假设nums1和nums2不会同时为空

思路：同88合并两个有序数组，然后分情况讨论中位数
"""


def find_median_sorted_array(nums1, nums2):
    m, n = len(nums1), len(nums2)
    p1, p2 = m - 1, n - 1
    p = m + n - 1
    for _ in range(n):
        nums1.append(0)
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    nums1[:p2+1] = nums2[:p2+1]
    if (m+n) % 2 != 0:
        return nums1[(m+n)//2]
    else:
        return (nums1[(m+n-1)//2]+nums1[(m+n)//2])/2


print(find_median_sorted_array([1, 3], [2]))



