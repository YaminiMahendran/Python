# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 19:27:57 2018

@author: yamini

"""
    def deleteDuplicates(self, head):
        if head == None:
            return head
            
        node = head
        
        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
                
        return head