# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 21:26:03 2018

@author: yamini

"""

from Linked_List_Creation import linkedList

list = linkedList()
list.insertAtBeginning(4)
list.display()
list.insertAtBeginning(3)
list.display()
list.insertAtEnd(2)
list.display()
print(list.size())
list.search(2)
print(list.search(2))

list.delete(3)
list.display()