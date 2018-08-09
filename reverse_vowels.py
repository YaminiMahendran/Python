class Solution(object):
    def reverseVowels(self, s):
        vowels=['a','e','i','o','u','A','E','I','O','U']
        new=[]
        final=[]
        revvowels=''
        i=-1
        for letter in s:
            if letter in vowels:
                new.append(letter)
        for letter in s:
            if letter not in vowels:
                final.append(letter)
            else:
                final.append(new[i])
                i -= 1
        revvowels =''.join(final)
        return revvowels
    
s=Solution()
print(s.reverseVowels('Mappye'))