#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/9 16:46
# @Author:   Domi
# @File:     exam605.py
# @Software: PyCharm

"""
605.《种花问题》（easy）

题目：假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数n 。能否在不打破种植规则的情况下种入n朵花？能
则返回True，不能则返回False

思路：2种
"""


def place_flowers_1(flowerbed, n):
    """
    法1：统计连续0的个数，要考虑首元素为0的情况
    :param flowerbed:
    :param n:
    :return:
    """
    tmp_1 = 0                             # 变量1统计插入1的个数
    tmp_2 = 1                             # 变量2统计连续0的个数
    for num in flowerbed:                 # 循环遍历
        if num == 0:                      # 如果元素为0
            tmp_2 += 1                    # 统计连续0的个数
        else:                             # 否则
            tmp_1 += abs(tmp_2 - 1) // 2  # 累加能插入1的数目
            tmp_2 = 0                     # 遇到1就归零
    return tmp_1 + tmp_2 // 2 >= n        # 返回逻辑值


def place_flowers_2(flowerbed, n):
    """
    法2：利用一个长度为3的滑窗，输入做padding
    :param flowerbed:
    :param n:
    :return:
    """
    flowerbed = [0] + flowerbed + [0]                              # 左右各增加一个空位置
    for i in range(1, len(flowerbed)-1):                           # 遍历出两端之外的位置
        if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:  # 遇到连续三个空位置
            flowerbed[i] += 1                                      # 放一盆花
            n -= 1                                                 # 花数减1
        if n <= 0:                                                 # 如果花用完了
            return True                                            # 返回True
    return False                                                   # 花没用完，返回False


print(place_flowers_2([1, 0, 0, 0, 1], 1))
