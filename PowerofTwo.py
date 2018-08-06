class Solution:
    def isPowerOfTwo(self, n):
        if n==1:
            return True
        elif n<=0:
            return False
        else:
            while(n>1):
                if n%2==0:
                    n=n/2
                    continue
                else:
                    return False
            return True
        
        
s=Solution()
print(s.isPowerOfTwo(-16))