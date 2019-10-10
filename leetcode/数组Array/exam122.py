#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/7/17 21:57
# @Author:   Domi
# @File:     exam122.py
# @Software: PyCharm

"""
122.买卖股票的最佳时机II（easy）

题目：给定一个数组，它的第i个元素是一支给定股票第i天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成
更多的交易（多次买卖一支股票）。

思路：上涨期间的第一天买入，下跌期间的前一天卖出，即可保证
最大利润。“阶梯效应”思想
"""


def max_profit(prices):
    """
    122.买卖股票的最佳时机II
    :param prices: 股票价格
    :return: profit
    """
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    print(profit)


real_price = [7, 1, 5, 3, 6, 4]
max_profit(real_price)
