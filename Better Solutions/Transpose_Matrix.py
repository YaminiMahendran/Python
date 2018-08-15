# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 18:34:34 2018

@author: yamini

"""
class Solution(object):
    def transpose(self,A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n,L=len(A),len(A[0])
        newmatrix=[[0]*n for i in range(L)]
        print (newmatrix)
        for i in range(n):
            for j in range(L):
                newmatrix[j][i]=A[i][j]
        return newmatrix
    
s=Solution()
print(s.transpose([[1,2,3],[4,5,6],[7,8,9]]))