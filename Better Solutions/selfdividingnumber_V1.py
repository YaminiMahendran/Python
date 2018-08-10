# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 19:03:00 2018

@author: yamini
"""

class Solution(object):
    def selfDividingNumbers(self, left, right):
        isselfdividing=lambda num: '0' not in str(num) and all([num%int(x)==0 for x in str(num)])
        return list(filter(isselfdividing,range(left,right+1)))

s=Solution()
print(s.selfDividingNumbers(1,22))