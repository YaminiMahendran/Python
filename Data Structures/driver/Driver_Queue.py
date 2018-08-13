# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:03:08 2018

@author: yamini

"""
from Queue_Implementation import Queue
q=Queue()
print(q.isempty())
q.enqueue(8)
q.enqueue('dog')
q.enqueue(-1)
print(q.display())
q.dequeue()
print(q.display())
q.dequeue()
print(q.display())
q.dequeue()
print(q.display())
print(q.size())
