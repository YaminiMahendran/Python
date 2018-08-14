# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:17:42 2018

@author: yamini

https://leetcode.com/problems/next-greater-element-i/discuss/97620/Python-solution-with-detailed-explanation
"""
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        cache, st = {}, []
        for x in nums:
            if len(st) == 0:
                st.append(x)
            elif x <= st[-1]:
                st.append(x)
            else:
                while st and st[-1] < x:
                    cache[st.pop()] = x
                st.append(x)
        result = []
        for x in findNums:
            if x in cache:
                result.append(cache[x])
            else:
                result.append(-1)
        return result


                    
s=Solution()
print(s.nextGreaterElement([2,4],[1,2,3,4]))