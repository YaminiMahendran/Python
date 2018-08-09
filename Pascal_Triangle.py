# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 15:23:45 2018

@author: yamini
"""
class Solution:
    def generate(self, numRows):
        l=[[1]*i for i in range(1,numRows+1)]
        if numRows < 3:
            return l
        for i in range(2,len(l)):
            for j in range(1,i):
                l[i][j]=l[i-1][j-1] +l[i-1][j]
        return l
            
        

s=Solution()
print(s.generate(6))
