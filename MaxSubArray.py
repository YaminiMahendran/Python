# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 11:31:06 2018

@author: yamini

"""
class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return 0
        maxsum=cursum=nums[0]
        for no in nums[1:]:
            cursum = max(no,no+cursum)
            maxsum = max(cursum,maxsum)
        return maxsum
    
s=Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))