# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 19:06:40 2018

@author: yamini

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
            if w <= a or w<= b or w<=c: 
                ans.append(word)
        return ans
s=Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))