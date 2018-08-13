# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:21:09 2018

@author: yamini

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Note : Use only stack operation (append,pop(no Insert))
"""
class MyQueue:

    def __init__(self):
        self.Inqueue =[]
        self.Outqueue=[]
        
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.Inqueue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty!= True:
            if (len(self.Outqueue)!=0):
                return self.Outqueue.pop()
            else:
                while(len(self.Inqueue)!=0):
                    self.Outqueue.append(self.Inqueue.pop())
                return self.Outqueue.pop()
        
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if (len(self.Outqueue)!=0):
            return self.Outqueue[-1]
        else:
            while(self.Inqueue!=[]):
                self.Outqueue.append(self.Inqueue.pop())
            return self.Outqueue[-1]
            
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.Inqueue==[] and self.Outqueue==[]

