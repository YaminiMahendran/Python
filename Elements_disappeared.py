# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 10:56:22 2018

@author: yamini
"""

class Solution:
    def findDisappearedNumbers(self, nums):
        new=set(nums)
        return [x for x in range(1,len(nums)+1) if x not in new ]
            
s=Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))