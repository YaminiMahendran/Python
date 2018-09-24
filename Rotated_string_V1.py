# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 11:23:29 2018

@author: yamini

"""
class Solution:
    def rotateString(self, A,B):
        if A == B:
            return True
        for i in range(len(A)):
            A = A[1:]+A[0]
            if A == B:
                return True
        return False 
        
s=Solution()
print(s.rotateString('abced','abecd'))