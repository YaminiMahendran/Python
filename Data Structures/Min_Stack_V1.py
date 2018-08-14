# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 22:29:47 2018

@author: yamini

Returns the minimum number in the stack after each push or pop

"""
class MinStack:

    def __init__(self):
        self.stack=[]
        self.min=float('inf')

    def push(self, x):
        if len(self.stack)==0:
            if (x)<self.min:
                self.min=x
                self.stack.append(x)
        else:
            if (x)<self.min:
                self.stack.append(self.min)
                self.min=x
            self.stack.append(x)
    
    def display(self):
        return self.stack 
        
    def pop(self):
        if self.isempty() == False:
            popped=self.stack.pop()
            if(popped==self.min):
              self.min= self.stack.pop()
            return popped
    
    def isempty(self):
        return len(self.stack) == 0
        
    def top(self): 
        if self.isempty() == False:
            return (self.stack[-1])
        

    def getMin(self):
         return self.min
        
"""
m=MinStack()
m.push(-2)
m.push(0)
# obj.pop()
# param_3 = obj.top()
print(m.gentMin())
"""