# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 20:02:53 2018

@author: yamini

"""
def Swap(x,y):
    x = x + y
    y = x - y
    x = x - y
    print("X:",x)
    print("Y:",y)

Swap(5,10)