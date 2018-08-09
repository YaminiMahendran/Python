# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 11:10:12 2018

@author: yamin
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
       return max([len(i) for i in "".join(str(n) for n in nums).split('0')])
        """
        max1=0
        count=0
        for each in nums:
            if each == 1:
                count +=1
            else:
                max1=max(count,max1)
                count=0
                
        return max1
        return (max(count,max1))
                
    
s=Solution()
print(s.findMaxConsecutiveOnes([1,0,0,1,1,0,1,1,1,1,0,1]))

