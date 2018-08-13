# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:50:38 2018

@author: yamini

"""
from Implement_Queue_using_Stack import MyQueue
q = MyQueue()
q.push(8)
q.push(1)
print(q.peek())
print(q.pop())
print(q.pop())
print(q.empty())
print(q.pop())
