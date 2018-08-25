# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 13:40:59 2018

@author: yamini

Logic:
     Use slow and fast pointers and at one point both slow and fast will meet 
     if its a cycle.
"""
class Solution(object):
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False