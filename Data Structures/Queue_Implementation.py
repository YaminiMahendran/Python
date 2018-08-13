# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 11:57:44 2018

@author: yamini

Queues are open from both ends meaning elements are added from the back and removed from the front
The element to be added first is removed first (First In First Out - FIFO)

"""
class Queue():
    def __init__(self):
        self.my_queue=[]
    
    def isempty(self):
        return self.my_queue==[]
    
    def enqueue(self,x):
        self.my_queue.insert(0,x)
        
    def dequeue(self):
        if self.isempty==True:
            print ("Queue is Empty")
        else:
            return self.my_queue.pop()
      
    def size(self):
        return len(self.my_queue)
    
    def display(self):
        return self.my_queue
        
        