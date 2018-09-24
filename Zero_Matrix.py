# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 16:36:23 2018

@author: yamini

"""
class Solution():
    
    def zero_out_row_col(mat):
      n = len(mat)
      if n == 0:
        return mat
      m = len(mat[0])
      zero_rows, zero_cols = [], []
      for r in xrange(n):
        for c in xrange(m):
          if mat[r][c] == 0:
            zero_rows.append(r)
            zero_cols.append(c)
            break
      for r in zero_rows:
        for c in xrange(m):
          mat[r][c] = 0
      for c in zero_cols:
        for r in xrange(n):
          mat[r][c] = 0
      print(mat)
        
s=Solution()
mat1 = [[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]
s.zero_out_row_col(mat1)