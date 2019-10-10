#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/20 14:07
# @Author:   Domi
# @File:     exam014.py
# @Software: PyCharm

"""
014.《最长公共前缀》（easy)

题目：编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串''

思路：两种
"""


def longest_common_prefix_1(strs):
    """
    法1：enumerate方法
    :param strs:["flower", "flow", "flight"]
    :return:fl
    """
    if not strs:                # if strs == None
        return ''               # 返回空
    s1 = min(strs)              # 数组中最小字符串
    s2 = max(strs)              # 数组中最大字符串
    for i, v in enumerate(s1):  # i是key，默认从0开始，v是value
        if v != s2[i]:          # 如果s1中的值不等于s2中的值
            return s2[:i]       # 字符串切片[:]
    return s1                   # 特殊情况，这里主要是针对输入是['']的情况


def longest_common_prefix_2(strs):
    """
    法2：zip函数，将对象打包成一个个元组
    :param strs:
    :return:
    """
    if not strs:
        return ''
    s = list(map(set, zip(*strs)))  # zip的逆过程 [{'f'}, {'l'}, {'i', 'o'}, {'g', 'w'}]
    res = ''                        # 定义一个空字符串
    for i, v in enumerate(s):       # enumerate返回的是set
        v = list(v)                 # set转换为list
        if len(v) > 1:              # 如果list长度大于1
            break                   # 直接退出循环
        res += v[0]                 # 否则写入res
    return res


print(longest_common_prefix_2(["flower", "flow", "flight"]))
