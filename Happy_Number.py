# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 17:30:12 2018

@author: yamini
"""
#if a number doesn't end with 1,it always ends up giving the same sum 
class Solution:
    def isHappy(self, n):
        m=set()
        while(n!=1):
            n=sum([int(i)**2 for i in str(n)])
            if n in m:
                return False
            else:
                m.add(n)
        else:
            return True
        
        
        
s=Solution()
print(s.isHappy(19))
        
        