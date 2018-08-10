# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 13:00:11 2018

@author: yamini

"""
class Solution:
    def uniqueMorseRepresentations(self, words):
        morse_alphabets = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        eng_morse_map = dict(zip("abcdefghijklmnopqrstuvwxyz", morse_alphabets ))
        return len({ "".join(eng_morse_map[c] for c in w) for w in words})# set {} is created to store so return 2
    
s=Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))