# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 19:06:40 2018

@author: yamini

The ordering operators (<, <=, >, >=) comoare two sets to determine their superset or subset relationship. 
These operators reflect the two definitions of subset (and superset). S1 is a subset of S2 if every element of S1 is in S2. The basic subset test is the <= operator; it says nothing about "extra" elements in S2. S1 is a proper subset of S2 if every element of S1 is in S2 and S2 has at least one additional element, not in S1. 
The proper subset test is the < operator.
"""
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a =set("qwertyuiop")
        b =set("asdfghjkl")
        c =set("zxcvbnm")  
        ans = []
        for word in words:
            w = set(word.lower())  
            if w <= a or w<= b or w<=c: # It determines the superset or subset relation 
                ans.append(word)
        return ans
s=Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))