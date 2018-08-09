class Solution(object):
    def moveZeroes(self, nums):
        """
        nums=sorted(nums,reverse=True)
        return nums
        """
        last0 = 0
        for i in range(0,len(nums)):
            if (nums[i]!=0):
                nums[i],nums[last0] = nums[last0],nums[i]
                last0+=1
        return nums
s=Solution()
print(s.moveZeroes([1,0,1]))