# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 16:13:23 2018

@author: yamini

"""
class Solution(object):
    def longestPalindrome(self, s):
        mydict = {}
        for each in s:
            mydict[each] = mydict.get(each,0)+1
        single = double = 0
        for val in mydict.values():
            if val % 2 == 0:
                double += val
            else:
                double += val -1
                single = 1
        return double + single

s=Solution()
print(s.longestPalindrome('abcddddc'))
                
