class Solution:
    def thirdMax(self, nums):
        nums=set(nums)
        nums=list(nums)
        nums.sort(reverse=True)
        if len(nums)>=3:
            return (nums[2])
        elif(len(nums)>0):
            return(nums[0])
        
s=Solution()
print(s.thirdMax([1,1,2,3]))