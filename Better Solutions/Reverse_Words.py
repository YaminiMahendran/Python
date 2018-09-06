# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:17:26 2018

@author: yamini

"""
class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.strip().split()[::-1])
            
            
s= Solution()
print(s.reverseWords("the sky is blue"))