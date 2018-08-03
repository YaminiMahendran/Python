class Solution:
    def lengthOfLastWord(self, s):
        s=s.strip()
        l1=[]
        l1=s.split(' ')
        if(len(l1)>=1):
            return (len(l1[-1]))
        else:
            return 0


        

s=Solution()
print(s.lengthOfLastWord('a '))
