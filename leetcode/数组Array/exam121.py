#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/17 16:17
# @Author : Domi
# @File : exam121.py
# @Software: PyCharm

"""
121.买卖股票的最佳时机（easy）

题目：给定一个数组，它的第i个元素是一支给定股票第i天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计
一个算法计算你所能获取的最大利润。不能在买入股票前卖出股票。

思路：a=min(a,b)，a=max(a,b)。这两个核心算式可以不断更新
当前值。
"""


def max_profit(prices):
    """
    121.买卖股票最佳时机
    :param prices: 股票价格
    :return: 最大利润profit
    """
    first = prices[0]
    profit = 0

    if not prices:  # if prices == 0，不是真，等价于为空
        print('价格为空！')

    for i in range(1, len(prices)):
        first = min(first, prices[i])
        profit = max(profit, prices[i]-first)
    print(profit)


real_price = [7, 1, 5, 3, 6, 4]
max_profit(real_price)
