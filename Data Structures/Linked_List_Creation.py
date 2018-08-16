# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 21:00:10 2018

@author: yamini

"""
from Node import Node
class linkedList():
    def __init__(self,head=None):
        self.head = head
    
    def insertAtBeginning(self,val):
        new_node = Node(val) # creates a node from class node
        new_node.setNext(self.head)
        self.head = new_node
        
    def insertAtEnd(self,val):
        new_node = Node(val)
        temp = self.head
        while(temp.getNext() != None):
            temp = temp.getNext()
        temp = temp.setNext(new_node)
    
    def size(self):
            temp=self.head
            count=1
            while(temp.getNext() != None):
                temp = temp.getNext()
                count += 1
            return count
        
    def search(self,data): # will it display address?
        temp=self.head
        found = False
        while temp and found is False: # wwhy temp condition?
            if temp.getValue() == data:
                found = True
            else:
                temp = temp.getNext()
        if temp is None:
            raise ValueError("Data not found ")
        return temp
    
    def delete(self,data):
        current = self.head
        found = False
        prev = None
        while current and found is False:
            if current.getValue() == data:
                found = True
            else:
                prev = current
                current = current.getNext()
        if current is None:
            raise ValueError("Data not Found")
        elif prev is None:
            self.head = current.getNext()
        else:
            prev.setNext(current.getNext())
            
                
        
        
    def display(self):
        temp = self.head
        l=[]
        while(temp != None): # why just temp?
            l.append(temp.getValue())
            temp = temp.getNext()
        print(l)
        
    