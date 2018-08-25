# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 14:15:25 2018

@author: yamini

Logic:
    find the length of List 1 and list 2. if the length are equal find
    at which point l1.next and l2.next are equal and return that node
    If not find the diff in length and start the lengthiest list from 
    the difference in position and repeat step 1

"""
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA,headB
        l1 = 0
        l2 = 0
        while curA is not None:
            l1 += 1
            curA = curA.next
        while curB is not None:
            l2 += 1
            curB = curB.next
        curA, curB = headA,headB
        if l1 > l2:
            for i in range(l1 -l2):
                curA = curA.next
        elif l2 > l1:
            for i in range(l2 -l1):
                curB = curB.next
        while (curA != curB):
            curA = curA.next
            curB = curB.next
        return curA
        
        
        