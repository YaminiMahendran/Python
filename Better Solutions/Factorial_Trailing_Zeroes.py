# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:58:46 2018

@author: yamini

meet the number that can be dived by 5, the Trailing will have 1 more zero.
2 .meet the number that can be dived by 5*5, the Trailing will have 2 more zero.
"""
class Solution(object):
    def trailingZeroes(self, n):
        tot = 0
        while(n > 0):
            n = n/5
            tot += n 
        return int(tot)
    
s=Solution()
print(s.trailingZeroes(100))