class Solution:
    def majorityElement(self, nums):
        n= (len(nums)/2)
        new={}
        for i,no in enumerate(nums):
            if no in new:
                new[no] += 1
            else:
                new[no] = 1
        l1=list(new.keys())
        l2=list(new.values())
        new_dict= dict(zip(l2,l1))
        max_no= max(l2)
        if max_no > n:
            return (new_dict[max_no])
        
s=Solution()
print(s.majorityElement([3,3,3,3,3,3,1,2,1,1]))
            