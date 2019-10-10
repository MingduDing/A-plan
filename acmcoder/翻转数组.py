#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/9/18 13:19
# @Author:   Domi
# @File:     翻转数组.py
# @Software: PyCharm

"""
题目描述
给定一个长度为n的整数数组a，元素均不相同，问数组是否存在这样一个片段，
只将该片段翻转就可以使整个数组升序排列。

输入
第一行数据是一个整数：n (1≤n≤105)，表示数组长度。
第二行数据是n个整数a[1], a[2], ..., a[n] (1≤a[i]≤109)。

样例输入
4
2 1 3 4

输出
输出“yes”，如果存在；否则输出“no”，不用输出引号。

样例输出
yes
"""

n = int(input())
x = [int(i) for i in input().split()]
y = [i for i in x]
y.sort()
partx = [x[i] for i in range(n) if x[i] != y[i]]
party = [y[i] for i in range(n) if x[i] != y[i]]

if partx[::-1] == party:
    print("yes")
else:
    print("no")

# n = int(input())
# list1 = []
# for i in input().split():
#     list1.append(int(i))
# list_sort = sorted(list1)
# list_length = len(list_sort)
# pos1 = 0
# pos2 = 1
#
# temp_list = []
# new_list = []
# while pos2 < list_length:
#     if list1[pos2] >= list1[pos2 - 1]:
#         if pos2 - pos1 == 1:
#             pos1 = pos2
#             pos2 += 1
#             break
#         else:
#             temp_list.insert(0, list1[pos1])
#             temp_list.reverse()
#             new_list = list1[0:pos1] + temp_list + list1[pos2:list_length]
#             break
#     else:
#         temp_list.append(list1[pos2])
#         pos2 += 1
#         if pos2 == list_length:
#             temp_list.insert(0, list1[pos1])
#             new_list = temp_list
#             new_list.reverse()
#             print(new_list)
#
# if new_list == list_sort or new_list == []:
#     print("yes")
# else:
#     print("no")
