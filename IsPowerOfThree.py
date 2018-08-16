# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 12:18:34 2018

@author: yamini

"""
class Solution:
    def isPowerOfThree(self, n):
        if n==1:
            return True
        elif n<=0:
            return False
        else:
            while(n>1):
                if n%3==0:
                    n=n/3
                    continue
                else:
                    return False
            return True