# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 18:46:38 2018

@author: yamini

"""
From Node import Node
def mergeTwoLists1(self, l1, l2):
    dummy = cur = Node(0)
    while l1 and l2:# and condition both list should have values else it will fail
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next# after breaking the loop cur will be in last pointer and l1 or l2 will append to it
    cur.next = l1 or l2 # check 0 or 1 elements 
    return dummy.next # bcoz we need dummy always to return the head
