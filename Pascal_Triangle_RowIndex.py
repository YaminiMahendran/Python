class Solution:
    def getRow(self, rowIndex):
        l=[[1]*i for i in range(1,rowIndex+2)]
        if rowIndex < 2:
            return l[-1]
        for i in range(2,len(l)):
            for j in range(1,i):
                l[i][j]=l[i-1][j-1] +l[i-1][j]
        return l[-1]
            
        

s=Solution()
print(s.getRow(0))