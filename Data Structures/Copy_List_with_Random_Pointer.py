# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 20:25:07 2018

@author: yamini

"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        map = {}
        iterNode = head
        while iterNode:
            map[iterNode] = RandomListNode(iterNode.label)
            iterNode = iterNode.next
        
        iterNode = head
        while iterNode:
            map[iterNode].next = map[iterNode.next] if iterNode.next else None
            map[iterNode].random = map[iterNode.random] if iterNode.random else None
            iterNode = iterNode.next
        return map[head] if head else None