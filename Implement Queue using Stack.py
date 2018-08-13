# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:21:09 2018

@author: yamini

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

"""
class MyQueue:

    def __init__(self):
        self.queue =[]
        
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        return self.queue.insert(0,x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.queue.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue(-1)

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.queue==[]:
        

