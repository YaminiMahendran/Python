# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 13:10:36 2018

@author: yamini

return sorted(num)[len(num)/2]
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.


"""
class Solution:
    def majorityElement(self, nums):
        majority_num = 0
        count = 0
        for num in nums:
            if count == 0:
                majority_num = num
            if majority_num != num:
                count -= 1
            else:
                count += 1
        return majority_num
"""
# two pass + dictionary
def majorityElement1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    for num in nums:
        if dic[num] > len(nums)//2:
            return num
    
# one pass + dictionary
def majorityElement2(self, nums):
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        if dic[num] > len(nums)//2:
            return num
        else:
            dic[num] += 1 
""" 
s=Solution()
print(s.majorityElement([0,1,2,3,4,5,0]))
            
