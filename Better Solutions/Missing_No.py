# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 15:13:28 2018

@author: yamini

"""
class Solution:
    def missingNumber(self, nums):
        return sum(list(range(len(nums)+1))) - sum(nums)
