class Solution:
    def findMaxConsecutiveOnes(self, nums):
        s=set(nums)
        t=list(s)
        print(t)
        new=[]
        count =1
        for i,each in enumerate(nums):
            if(i != len(nums)-1):
                if (each==1) and (nums[i+1]==1):
                    count += 1
                    new.append(count)
                else:
                    count=1
        if len(new)!= 0:
            return max(new)
        elif len(nums)==0: 
            return 0
        elif len(nums)==1 and nums[0]==1:
            return 1
        elif len(nums)==1 and nums[0]==0:
            return 0
        elif 1 in t:
            return 1
        elif t[0]==0 or t[1]==0:
            return 0
        

s=Solution()
print(s.findMaxConsecutiveOnes([0,1]))