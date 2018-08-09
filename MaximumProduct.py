# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 12:37:48 2018

@author: yamini
"""

class Solution:
    def maximumProduct(self, nums):
        if(len(nums)==3):
            return nums[-1]*nums[-2]*nums[-3]
        l1=sorted(nums,reverse=True)
        l2=sorted(nums,reverse=False)
        print(l1[0:3],l2[0:3])
        return max(l1[0]*l1[1]*l1[2],l1[0]*l2[0]*l2[1])
        
        
s=Solution()
print(s.maximumProduct([-4,-3,-2,-1,60]))