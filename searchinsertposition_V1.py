# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 15:49:50 2018

@author: yamin
"""
class Solution:
    def searchInsert(self, nums, target):
        for i,no in enumerate(nums):
            if no== target:
                return i
            elif no > target:
                return i 
        return -1
        
        #return len([x for x in nums if x < target])
    
s=Solution()
print(s.searchInsert([1,3,5,6],0))