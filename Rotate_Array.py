# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:43:00 2018

@author: yamini

A little important thing to be cautious:

nums[:] = nums[n-k:] + nums[:n-k] 
can't be written as:

nums = nums[n-k:] + nums[:n-k]
The previous one can truly change the value of old nums, but the following one just changes its reference to a new nums not the value of old nums.
"""
class Solution:
    def rotate(self, nums, k):
        while(k>0):
            nums[:] = nums[-1:]+nums[0:-1]
            k -= 1
        return (nums)
    
"""n = len(nums) - k  
        nums[:] = nums[n:] + nums[:n]
"""
        
s=Solution()
print(s.rotate([-1,-100,3,99],2))