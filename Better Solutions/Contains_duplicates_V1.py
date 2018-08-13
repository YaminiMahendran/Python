class Solution:
    def containsDuplicate(self, nums):
        new={}
        for i in nums:
            if i not in nums:
                new[i]=1
            else:
                return True
        return False
        
s=Solution()
print (s.containsDuplicate([1,2]))