class Solution:
    def isPalindrome(self, x):
        Reverse = 0
        z=x
        while(x > 0):
            Reminder = x %10
            Reverse = (Reverse *10) + Reminder
            x = x //10
        y=Reverse
        print (y)
        if(y==z):
            return True
        else:
            return False
s=Solution()
print(s.isPalindrome(12))