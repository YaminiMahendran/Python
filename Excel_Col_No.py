# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 14:52:27 2018

@author: yamini

"""
class Solution(object):
    def titleToNumber(self, s):
        s=s[::-1]
        sum = 0
        for i,alpha in enumerate(s):
            sum += (ord(alpha)-65 +1) * (26**i)
        return sum
        
        
s=Solution()
print(s.titleToNumber('AB'))