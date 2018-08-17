# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:06:50 2018

@author: yamini

"""
class Solution:
    def twoSum(self, nums, target):
        list1=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if target - nums[i] == nums[j]:
                    if i != j:
                        list1.extend([i,j])
                        break
        return list1
                
s=Solution()
print(s.twoSum([2, 7, 11, 15],9))