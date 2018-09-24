# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 16:47:53 2018

@author: yamini

"""
class Solution:
    def shortestToChar(self, S, C):
        new=[]
        final=[]
        for i,no in enumerate(S):
            if no==C:
                new.append(i)
        print(new)
        for i in range(len(S)):
            final.append(min([abs(j-i) for j in new]))
            print(final)
        return final
                 
        
        
s=Solution()
print(s.shortestToChar("loveleetcode",'e'))