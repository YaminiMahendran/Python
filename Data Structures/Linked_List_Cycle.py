# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 13:40:59 2018

@author: yamini

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