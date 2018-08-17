# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:43:00 2018

@author: yamini

"""
class Solution:
    def rotate(self, nums, k):
        while(k>0):
            nums = nums[-1:]+nums[0:-1]
            k -= 1
        return (nums)
        
s=Solution()
print(s.rotate([-1,-100,3,99],2))