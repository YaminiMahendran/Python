# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 13:10:05 2018

@author: yamini

"""
import string
class Solution:
    def mostCommonWord(self, paragraph, banned):
        ban = set(banned)
        paragraph = [s.strip("!?',;.") for s in paragraph.lower().split(' ')]        
        p = [w for w in paragraph if w not in ban]
        word_count = {w: 0 for w in p}
        for w in p:
            word_count[w] += 1
        return max(word_count, key=lambda k: word_count[k])
   
    
s=Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit",["hit"]))