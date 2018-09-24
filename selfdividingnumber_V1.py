# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 19:03:00 2018

@author: yamini
"""

class Solution(object):
    def selfDividingNumbers(self, left, right):
        result =[]
        for x in range(left,right+1):
            if is_selfdividing(x):
                result.append(x)
        return result

def is_selfdividing(x):
    for no in str(x):
        if no == "0" or int(x)%int(no)!=0:
            return False
    return True
        
"""
isselfdividing=lambda num: '0' not in str(num) and all([num%int(x)==0 for x in str(num)])
return list(filter(isselfdividing,range(left,right+1)))
"""
    


s=Solution()
print(s.selfDividingNumbers(1,22))