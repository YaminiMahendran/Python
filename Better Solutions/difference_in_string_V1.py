# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 12:57:06 2018

@author: yamini
"""

class Solution(object):
    def findTheDifference(self, s, t):
        return [i for i in t if i not in s or s.count(i)!=t.count(i)][0]#it will print [a,a] in that 0th position is a
        """
        for i in t:
            if i not in s or s.count(i)!=t.count(i):
                return i
        """
        
        
s=Solution()
print(s.findTheDifference('a','aa'))