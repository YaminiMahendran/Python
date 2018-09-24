# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 20:16:00 2018

@author: yamini

# Array is sorted 
"""
def Missing_No(A):
    n = len(A)
    total = (n+1) * (n+2) / 2
    sum_A = sum(A)
    return total - sum_A

A=[1,2,4,5,6]
missing_no = int(Missing_No(A))
print(missing_no)
    