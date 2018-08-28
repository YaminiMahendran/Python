# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 12:37:15 2018

@author: yamini

"""
class Solution:
    # @return a string
    def convertToTitle(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.insert(0,capitals[(num-1)%26])
            num = (num-1) // 26
        return ''.join(result)
    
s=Solution()
print(s.convertToTitle(702))
        
    