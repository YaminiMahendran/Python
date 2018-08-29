class Solution(object):
    def detectCapitalUse(self, word):
        if (word.upper()==word or word==word.lower()):
            return True
        elif(word[0]==word[0].upper() and word[1:]==word[1:].lower()):
            return True
        else:
            return False
        
s=Solution()
print(s.detectCapitalUse('MaC'))
