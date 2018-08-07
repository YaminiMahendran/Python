class Solution:
    def multiply(self, num1, num2):
        value = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        res1=0
        res2=0
        prod=0
        for digit in str(num1):
            res1=res1*10 +value[digit]
        for digit in str(num2):
            res2=res2*10 +value[digit]
        prod= res1* res2
        return str(prod)
        
    
        
            
s=Solution()
print(s.multiply(123,456))