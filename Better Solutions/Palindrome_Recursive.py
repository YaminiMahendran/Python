# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 19:41:16 2018

@author: yamini

"""
def is_Palindrome(a):
    if len(a)<1:
        return True
    else:
        if(a[0]==a[-1]):
            return is_Palindrome(a[1:-1])
        else:
            return False
a=str(input("Enter a String:"))
if(is_Palindrome(a)== True):
    print("String is a Palindrome")
else:
    print("String is not a Palindrome")
        
