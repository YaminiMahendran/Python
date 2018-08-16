# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 10:55:48 2018

@author: yamini

"""
class Solution:
    def rotateString(self, A,B):
        count = len(A) - 1
        if len(A) == 0 and len(B)==1:
            return False
        if len(A)==0:
            return True
        temp = A
        l=[]
        while (count > 0):
            temp = temp[1:] + temp[0]
            l.append(temp)
            count -= 1
        if B in l:
            return True
        return False
        
s=Solution()
print(s.rotateString('abcde','bcdeaa'))