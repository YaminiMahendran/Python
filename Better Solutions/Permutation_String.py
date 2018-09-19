# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 15:16:52 2018

@author: yamini

"""
class Solution:
    def Permuation(self, s1,s2):
        dict1 = {}
        for ltr in s1:
            dict1[ltr] = dict1.get(ltr,0) + 1
        for ltr in s2:
            if ltr not in dict1.keys():
                return False
            dict1[ltr] -= 1
            if dict1[ltr]==0:
                del dict1[ltr]
        return len(dict1)==0
            
            
        
s=Solution()
print(s.Permuation("latin","inlat1"))