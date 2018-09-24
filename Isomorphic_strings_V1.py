# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 15:43:17 2018

@author: yamini
return [s.find(i) for i in s] == [t.find(j) for j in t]

"""
class Solution:
    def isIsomorphic(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val,[]) + [i]
        print (d1)
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        print (d2)
        return sorted(d1.values()) == sorted(d2.values())
        
s=Solution()
print(s.isIsomorphic('aba','dbd'))
