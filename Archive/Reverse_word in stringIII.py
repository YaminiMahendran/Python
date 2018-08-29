class Solution(object):
    def reverseWords(self, s):
        new=""
        new1=""
        new=s.split(" ")
        for each in new:
            new1 +=(each[::-1]) +" "
        return new1.rstrip(" ")