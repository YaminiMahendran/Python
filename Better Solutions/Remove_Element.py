# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 14:06:24 2018

@author: yamini

"""
class Solution(object):
    def removeElement(self, a, val):
        j = 0
        for i in range(len(a)):
            if a[i] != val:
                a[j] = a[i]
                j += 1
        return j
        

s=Solution()
print(s.removeElement([3,2,2,3],3))