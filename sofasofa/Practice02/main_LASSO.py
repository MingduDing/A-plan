#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/7/24 15:15
# @Author:   Domi
# @File:     main_LASSO.py
# @Software: PyCharm

"""
题目：交通事故理赔审理

任务类型：二元分类

背景介绍:
在交通摩擦（事故）发生后，理赔员会前往现场勘察、采集信息，这些信息往往
影响着车主是否能够得到保险公司的理赔。训练集数据包括理赔人员在现场对该
事故方采集的36条信息，信息已经被编码，以及该事故方最终是否获得理赔。我
们的任务是根据这36条信息预测该事故方没有被理赔的概率。

数据来源：
某汽车大数据网站

方法：LASSO逻辑回归模型
"""

# 引入模块
from sklearn.linear_model import LogisticRegression
import pandas as pd

# 导入数据
train = pd.read_csv('./data/train.csv')
test = pd.read_csv('./data/test.csv')
submit = pd.read_csv('./data/sample_submit.csv')

# 删除id
train.drop('CaseId', axis=1, inplace=True)
test.drop('CaseId', axis=1, inplace=True)

# 取出训练集中的y
y_train = train.pop('Evaluation')

# 建立LASSO逻辑回归模型
clf = LogisticRegression(penalty='l1', C=1.0, random_state=0)
# penalty：使用指定正则化项(默认：l2)
# C：正则化强度的反，值越小正则化强度越大
# random_state：随机数生成器
clf.fit(train, y_train)
y_pred = clf.predict_proba(test)[:, 1]

# 输出预测结果至my_LASSO_prediction.csv
submit['Evaluation'] = y_pred
submit.to_csv('my_LASSO_prediction.csv', index=False)
