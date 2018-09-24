# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 14:30:07 2018

@author: yamin
"""

class Solution(object):
    def numJewelsInStones(self, J, S):
        return sum(s in J for s in S)
    
s=Solution()
print(s.numJewelsInStones('z','zZZ'))