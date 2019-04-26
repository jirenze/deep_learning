# -*- coding: utf-8 -*-
"""
Created on Fri. April.26 2019

@author: jirenze
"""
import tensorflow as tf

a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")
result = a+b
print(result)