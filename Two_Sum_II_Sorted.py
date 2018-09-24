# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 09:51:52 2018

@author: yamini

Have two pointer one from front and another from last

add front and small until small is < large

if the sum is greater than target then decrement the large by 1 index
if smaller increase the small by 1 index

"""
class Solution(object):
    def twoSum(self, numbers, target):
        first = 0
        last  = len(numbers)-1
        while (first < last):
            sum=numbers[first]+numbers[last]
            if(sum == target):
                return [first+1,last+1]
            elif(sum > target):
                last -= 1
            else:
                first += 1
       
        
s=Solution()
print(s.twoSum([2,7,11,15],9))