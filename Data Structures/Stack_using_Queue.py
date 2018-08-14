# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 10:08:47 2018

@author: yamini

"""
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.enqueue(x)
        for i in range(0,self.queue.size()):#for each push rotate the queue
            self.queue.enqueue(self.queue.dequeue())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue.dequeue()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue.peek()

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue.isempty()
        
class Queue():
    def __init__(self):
        self.my_queue=[]
    
    def isempty(self):
        return self.my_queue==[]
    
    def enqueue(self,x):
        self.my_queue.insert(0,x)
        
    def dequeue(self):
        if self.isempty==True:
            return
        else:
            return self.my_queue.pop()
      
    def size(self):
        return len(self.my_queue)
    
    def peek(self):
        return self.my_queue[-1]
    
    def display(self):
        return self.my_queue
