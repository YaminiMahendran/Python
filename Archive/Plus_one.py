class Solution:
    def plusOne(self, digits):
        new=''
        l1=[]
        l2=[]
        for x in digits:
            new += str(x)
        l1=int(new)+1
        print(l1)
        for each in str(l1):
            l2.append(int(each))
        return(l2)

s=Solution()
print(s.plusOne([4,3,2,1]))