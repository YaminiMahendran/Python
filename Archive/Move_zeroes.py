class Solution(object):
    def moveZeroes(self, nums):
        count=0
        new_list=[]
        for number in nums:
            if number==0:
                count += 1 
            else:
                new_list.append(number)
        while(count>0):
            new_list.append(0)
            count -=1
        for i,each in enumerate(new_list):
            nums[i]=new_list[i]