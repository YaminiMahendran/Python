# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 11:24:48 2018

@author: yamini

"""
def secondLargest(arr):
    largest = arr[0]
    second = arr[0]
    for i,no in enumerate(arr):
        if arr[i] > largest :
            second = largest
            largest = arr[i]
        elif arr[i] > second:
            second = arr[i]
    return second
    

arr=[14,46,47,85,92,52,48,36,66,86]
s= secondLargest(arr)
print(s)