#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/13 16:33
# @Author:   Domi
# @File:     exam667.py
# @Software: PyCharm

"""
667.《优美的排列II》（medium）

题目：给定两个整数n和k，你需要实现一个数组，这个数组包含从1到n的n个不同整数，同时满足以下条件：
1）如果这个数组是[a1,a2,a3,...,an]，那么数组[|a1 - a2|,|a2 - a3|,|a3 - a4|,...,|an-1 - an|]中应该有且仅有k个不同整数；.
2）如果存在多种答案，你只需实现并返回其中任意一种

思路：5个元素能够组成的最大不同差值序列为4，即[1,2,3,4,5]——>[1,5,2,4,3]
"""


def construct_array(n, k):
    if k == 1:                        # 如果k=1
        return list(range(1, n+1))    # 直接构造等差数列
    else:                             # 否则
        tmp = [1]                     # 创建一个单独的列表
        nums = list(range(2, n+1))    # 构造[2,3,...,n]的等差数列列表
        for i in range(k-1):          # 循环遍历
            if i % 2 == 0:            # 如果i是偶数
                tmp.append(nums[-1])  # nums的尾元素插入到tmp中
                nums.pop(-1)          # 删除nums尾元素
            else:                     # 如果i是奇数
                tmp.append(nums[0])   # nums的首元素插入到tmp中
                nums.pop(0)           # 删除nums首元素
        if k % 2 == 1:                # 如果k是奇数
            return tmp+nums           # 合并tmp和nums返回
        else:                         # 如果k是偶数
            nums.reverse()            # nums反转，倒序
            return tmp+nums           # 合并tmp和nums返回


print(construct_array(6, 3))
