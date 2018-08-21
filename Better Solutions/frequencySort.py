# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 16:41:32 2018

@author: yamini

"""
import operator
class Solution:
    def frequencySort(self, s):
        dict1,l1={},''
        for letter in s:
            dict1[letter] =dict1.get(letter,0) + 1
        sorted_dict = sorted(dict1.items(),key=operator.itemgetter(1) ,reverse=True)
        #print(sorted_dict)
        for ltr in sorted_dict:
            l1 += ltr[0] * ltr[1]
        return(l1)
           
            

s=Solution()
print(s.frequencySort("aaaccc"))