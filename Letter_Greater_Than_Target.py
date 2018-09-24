# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 16:54:51 2018

@author: yamini

"""
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        start = 0
        end = len(letters)-1
        if target >= letters[end] or target < letters[start]:
            return letters[start]

        while(start + 1 < end):
            mid = int((start+end)/2)
            if letters[mid] >= target:
                end = mid
            if letters[mid] <= target:
                start = mid

        while(letters[start] == target):
            start = start+1

        if letters[start-1] == target:
            return letters[start]

        return letters[end]
        
s=Solution()
print(s.nextGreatestLetter(["f", "i", "c"],"a"))
        