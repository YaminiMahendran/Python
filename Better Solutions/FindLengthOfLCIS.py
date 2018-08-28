# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 11:57:22 2018

@author: yamini

"""
class Solution(object):
    def findLengthOfLCIS(self, nums):
        prev =nums[0]
        cur = 1
        tot = 1
        for i in range(1,len(nums)):
            if(nums[i] > prev):
                cur += 1
                tot = max(cur,tot)
            else:
                cur = 1
            prev = nums[i]
        return tot

s=Solution()
print(s.findLengthOfLCIS([1,3,5,4,7]))
        