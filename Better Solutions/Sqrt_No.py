# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 15:48:58 2018

@author: yamini

"""
class Solution(object):
    def mySqrt(self, x):
        no = x
        while no * no > x:
            no = (no + x/no) /2
        return no
    
s=Solution()
print(s.mySqrt(2))