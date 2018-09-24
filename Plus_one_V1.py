class Solution:
    def plusOne(self,digits):
        num = 0
        for i in range(len(digits)):
            num+= digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]
    """
    return list(map(int, str(int(''.join(map(str, digits)))+1)))


    """


s=Solution()
print(s.plusOne([4,3,2,1]))