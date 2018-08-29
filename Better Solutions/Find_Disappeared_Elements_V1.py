# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 09:26:09 2018

@author: yamini

Traverse each no and find its corresponding index ex.if 4 its index is 3.
Update the no in 3rd index as -3 and repeat .While reading take the abs value .
if the value is already neg take abs and update it as neg again
after loop , only the no's which disappeared will not have index (i+1)
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
    
s=Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))