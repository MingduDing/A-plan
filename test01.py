# -*- coding: utf-8 -*-
# @Time : 2019/7/17 9:33
# @Author : Domi

"""
计算二元二次函数最小值
"""

import tensorflow as tf

x = tf.Variable(tf.constant(-1.5, dtype=tf.float32))
y = tf.Variable(tf.constant(0.5, dtype=tf.float32))

z = tf.square(3+(y/x)*2) + tf.square(3+x/y)

train_step = tf.train.GradientDescentOptimizer(0.2).minimize(z)


with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    for i in range(400):
        sess.run(train_step)
        x_val = sess.run(x)
        y_val = sess.run(y)
        z_val = sess.run(z)
        print("After %s steps: x is %f,  y is %f, z is %f." % (i, x_val, y_val, z_val))