class Solution(object):
    def singleNumber(self, nums):
        num_count={}
        for each in nums:
            num_count[each] =num_count.get(each,0)+1
        print num_count
        for each in num_count:
            if num_count[each]==1:
                return each
            else:
                pass
        

                
        