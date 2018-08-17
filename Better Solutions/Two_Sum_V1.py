# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:06:50 2018

@author: yamini

"""
class Solution:
    def twoSum(self, nums, target):
        dict={}
        for i,no in enumerate(nums):
            if target - no in dict:
                return [dict[target-no],i]
            dict[no] = i
                
s=Solution()
print(s.twoSum([2, 7, 11, 15],9))