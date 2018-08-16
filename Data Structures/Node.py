# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 10:47:12 2018

@author: yamini

"""
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
        
    def setValue(self,x):
        self.value = x
        
    def getValue(self):
        return self.value
    
    def setNext(self,y):
        self.next = y
    
    def getNext(self):
        return self.next