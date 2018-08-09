# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 12:29:15 2018

@author: yamin
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.upper()==word or word[1:].lower()==word[1:] or word.lower()==word
    
s=Solution()
print(s.detectCapitalUse("leet"))