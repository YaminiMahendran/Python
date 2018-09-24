class Solution:
    def containsDuplicate(self, nums):
    """
        numsSet=set(nums)
        if len(nums) == len(numsSet):
            return False
        return True     
    """
    my_dict = {}
        for element in nums:
            if element not in my_dict:
                my_dict[element] = 1
            else:
                return True
        return False
        
s=Solution()
print (s.containsDuplicate([3,1]))