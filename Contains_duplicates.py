class Solution:
    def containsDuplicate(self, nums):
        new=[]
        dup=[]
        for each in nums:
            if each not in new:
                new.append(each)
            else:
                dup.append(each)
        if len(dup)>=1:
            return True
        else:
            return False
        
s=Solution()
print (s.containsDuplicate([]))