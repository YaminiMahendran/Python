# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 17:22:05 2018

@author: yamini

"""
class Solution:
    def isValid(self, s):
        my_list=[]
        for each in s:
            if each=='(' or each=='[' or each =='{':
                my_list.append(each)
            elif each==')' or each==']' or each =='}':
                if (len(my_list) !=0):
                    popped=my_list.pop()
                    print(popped)
                    if popped =='(' and each !=')' or popped =='[' and each !=']' or popped =='{' and each !='}':
                        return False
                else:
                    return False
            else:
                return False
        if(len(my_list)==0):
            return True
        else:
            return False
    
    
    

        

s=Solution()
print(s.isValid('({}[])'))