# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 16:20:14 2018

@author: yamini

"""
class Solution:
    def firstUniqChar(self, s):
        dict1={}
        for letter in s:
            dict1[letter] =dict1.get(letter,0) + 1
        for idx,ltr in enumerate(s):
            if dict1[ltr] == 1:
                return idx
        return -1
                
            

s=Solution()
print(s.firstUniqChar("leetcodelove"))