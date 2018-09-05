# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 17:32:44 2018

@author: yamini

"""
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = list(S)
        solutions = ['']
        while S:
            last = S.pop()
            if last.isalpha():
                solutions = [last.lower() + x for x in solutions] + [last.upper() + x for x in solutions]
                print(solutions)
            else:
                solutions = [last + x for x in solutions]
                print (solutions)
        return solutions
    
s=Solution()
print(s.letterCasePermutation("2ba"))