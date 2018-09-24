# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 17:56:11 2018

@author: yamini
1+3+5+ ... +(2n-1)
"""
class Solution:
    def isPerfectSquare(self, num):
        i=1
        while(num > 0):
            num -= i
            i +=2
        return (num==0)
        
s=Solution()
print(s.isPerfectSquare(13))