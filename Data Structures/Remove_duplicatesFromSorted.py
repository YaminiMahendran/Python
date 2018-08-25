# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 19:27:57 2018

@author: yamini

"""
def deleteDuplicates(self, head):
    cur = head
    while cur:
        while cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next     # skip duplicated node
        cur = cur.next     # not duplicate of current node, move to next node
    return head