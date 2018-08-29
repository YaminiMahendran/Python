# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 17:42:36 2018

@author: yamini

"""
class Solution(object):
    def reverseVowels(self, s):
        vowels=['a','e','i','o','u','A','E','I','O','U']
        new=list(s)
        p1 = 0 
        p2 = len(new)-1
        while(p1 < p2):
            if new[p1] in vowels and new[p2] in vowels:
                new[p1],new[p2] = new[p2],new[p1]
                p1 +=1
                p2 -=1
            if new[p1] not in vowels:
                p1 +=1
            if new[p2] not in vowels:
                p2 -=1
        return ''.join(new)
                
s=Solution()
print(s.reverseVowels('Mappye'))