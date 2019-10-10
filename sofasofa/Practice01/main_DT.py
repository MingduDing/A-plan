#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/7/23 15:03
# @Author:   Domi
# @File:     main_DT.py
# @Software: PyCharm

"""
题目：公共自行车使用量预测

任务类型：回归

背景介绍:
公共自行车低碳、环保、健康，并且解决了交通中“最后一公里”的痛点，
在全国各个城市越来越受欢迎。本练习赛的数据取自于两个城市某街道
上的几处公共自行车停车桩。我们希望根据时间、天气等信息，预测出
该街区在一小时内的被借取的公共自行车的数量。

数据来源：
Laboratory of Artificial Intelligence and Decision Support (LIAAD),
University of Porto, Portugal。为了公平起见，数据已经进行脱敏加工处理。

方法：决策树回归模型
"""

# 引入模块
from sklearn.tree import DecisionTreeRegressor
import pandas as pd

# 读取数据
train = pd.read_csv('./data/train.csv')
test = pd.read_csv('./data/test.csv')
submit = pd.read_csv('./data/sample_submit.csv')

# 删除id
train.drop('id', axis=1, inplace=True)
test.drop('id', axis=1, inplace=True)

# 读取训练集的y
y_train = train.pop('y')

# 建立最大深度为5的决策树回归模型
reg = DecisionTreeRegressor(max_depth=5)
reg.fit(train, y_train)
y_pred = reg.predict(test)

# 输出预测结果至my_DT_prediction.csv
submit['y'] = y_pred
submit.to_csv('my_DT_prediction.csv', index=False)

