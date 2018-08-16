# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 21:00:10 2018

@author: yamini

"""
from class_Node import Node

class LinkedList:
        def __init__(self):
            self.head = None
            
        def insertAtBeginning(self,value):
            temp = Node(value)#create node
            temp.setNext(self.head)
            self.head = temp
            
        def insertAtEnd(self,value):
            temp = Node(value)
            temp1 = self.head
            while(temp1.getNext() != None):#temp1 refers address
                temp1 = temp1.getNext()
            temp1.setNext(temp)
            
        def size(self):
            temp=self.head
            count=0
            while(temp.getNext() != None):
                temp = temp.getNext()
                count += 1
            return count
            
            
            
        def print(self):
            temp = self.head
            while(temp != None):#doubt in temp?
                print (temp.getValue())
                temp = temp.getNext()
