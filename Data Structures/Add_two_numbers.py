# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 20:22:08 2018

@author: yamini

"""
def addTwoNumbers(self, l1, l2):
    carry , sum = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        sum  = v1+v2+carry
        carry = sum /10
        val = sum % 10
        n.next = ListNode(val)
        n = n.next
    return root.next
