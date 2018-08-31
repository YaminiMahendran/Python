# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 21:56:39 2018

@author: yamini

"""
class Solution(object):
    def addDigits(self, num):
         if num ==0:
             return num
         if num%9==0:
             return 9
         else:
             return num%9
         
s=Solution()
print(s.addDigits(17))