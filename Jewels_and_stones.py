class Solution(object):
    def numJewelsInStones(self, J, S):
        count=0
        for letter in S:
            for word in J:
                if word==letter:
                    count += 1
        return count 
        
"""
Input: J = "z", S = "ZZ"
Output: 0
"""