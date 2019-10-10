#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/9/16 14:06
# @Author:   Domi
# @File:     股神.py
# @Software: PyCharm

"""
题目描述
经过严密的计算，小赛买了一支股票，他知道从他买股票的那天开始，股票会有以下变化：第一天不变，以后涨一天，
跌一天，涨两天，跌一天，涨三天，跌一天...依此类推。为方便计算，假设每次涨和跌皆为1，股票初始单价也为1，
请计算买股票的第n天每股股票值多少钱？

输入
输入包括多组数据；每行输入一个n，1<=n<=10^9。
样例输入
1
2
3
4
5

输出
请输出他每股股票多少钱，对于每组数据，输出一行。
样例输出
1
2
1
2
3
"""


def foo(days):
    n = 0
    count = 0
    if days == 1:
        res = 1
    else:
        while n * (n-1) <= 2 * days:
            n += 1
            count = n - 3
        res = days - 2 * count
    return res


while True:
    a = int(input())
    print(foo(a))


# a = int(input())
#
# class Fun:
#     def __init__(self):
#         self.a = 3
#         self.b = 3
#
#     def __next__(self):
#         self.a = self.a + self.b
#         self.b += 1
#         return self.a
#
#     def __iter__(self):
#         return self
#
#
# fun = Fun()
# n = 1
# for i in fun:
#     if i <= a:
#         n = n + 1
#     else:
#         break
# result = a - n * 2
# print(result)
