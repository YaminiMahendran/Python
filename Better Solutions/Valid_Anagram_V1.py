# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 14:25:18 2018

@author: yamini
"""

class Solution(object):
    def isAnagram(self,s,t):
        s_dict={}
        t_dict={}
        for letter in s:
            s_dict[letter] =s_dict.get(letter,0) +1
        for letter in t:
            t_dict[letter]=t_dict.get(letter,0)+1
        return (s_dict==t_dict)
    
    """
    return sorted(s)==sorted(t)
    """
        
s=Solution
print(s.isAnagram( "anagram" ,"abc","acb"))