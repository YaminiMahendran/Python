# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 20:25:55 2018

@author: yamini

"""
class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
    def setValue(self,x):
        self.value=x
    def getValue(self):
        return self.value
    def setNext(self,y):
        self.next= y
    def getNext(self):
        return self.next
        