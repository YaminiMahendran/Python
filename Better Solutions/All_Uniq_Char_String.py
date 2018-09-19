# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 15:25:23 2018

@author: yamini

"""
class Solution():
    def contains_no_duplicates(x):
      letters = {}
      for letter in x:
        if letter in letters:
          return False
        letters[letter] = True
      return True
  
s=Solution()
print(s.contains_no_duplicates('yamini'))
