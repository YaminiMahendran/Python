# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 15:08:03 2018

@author: yamini
"""
class Solution:
    def thirdMax(self, nums):   
        first = second = third = float('-inf')
        for num in nums:
            if num == first or num == second or num == third:
                continue
            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num
        return third if third!=float('-inf') else first

s=Solution()
print(s.thirdMax([1,2]))