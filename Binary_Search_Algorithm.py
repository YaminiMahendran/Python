# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:43:12 2018

@author: yamini

"""
def binarySearch(arr,l,r,x):
    while (l <= r):
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid +1
        else:
            r = mid - 1
    return -1
arr =[2,3,4,10,20,40]
x=2
b = binarySearch(arr,0,len(arr)-1,x)
if(b != -1):
    print("Element is present at index %d" %b)
else:
    print("Element is not present in the array")