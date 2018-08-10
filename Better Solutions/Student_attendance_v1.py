# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 16:39:38 2018

@author: yamini
"""

class Solution:
    def checkRecord(self, s):
            return not (s.count('A') > 1 or 'LLL' in s)


s=Solution()
print(s.checkRecord("PPALLL"))