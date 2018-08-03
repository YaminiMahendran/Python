class Solution:
    def findDisappearedNumbers(self, nums):
        new=[]
        disappear=[]
        if len(nums) != 0:
            for i in range(min(nums),max(nums)+1):
                new.append(i)
        for element in new:
            if element not in nums:
                disappear.append(element)
            else:
                pass
        return (disappear)
        
        
        
s=Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))