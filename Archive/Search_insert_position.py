class Solution:
    def searchInsert(self, nums, target):
        new=[]
        for i,no in enumerate(nums):
            if nums[i]==target:
                return i
            elif(max(nums)<target):
                return len(nums)
            else:
                #print('p')
                if nums[i]< target:
                   pass
                else:
                    new.append(no)
                    #print(3)
            if len(new)!=0:
                return nums.index(new[0])


s=Solution()
print(s.searchInsert([1,3,5,6],0))