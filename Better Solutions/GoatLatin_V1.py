class Solution:
    def toGoatLatin(self, S):
        return " ".join([x[1:]+x[0]+"ma"+"a"*(y+1) if x[0] not in "aeiouAEIOU" else x+"ma"+"a"*(y+1) for y,x in enumerate(S.split(" "))])
    """
    def toGoatLatin(self, S):
        word_list = S.split()
        for i in range(len(word_list)):
            if word_list[i][0].lower() in ['a','e','i','o','u']:
                word_list[i] = word_list[i] + 'ma' +(i+1)*'a'
            else:
                word_list[i] = word_list[i][1:] + word_list[i][0] + 'ma' + (i+1)*'a'
        result = ' '.join(word_list)
        return result
    """
s=Solution()
print(s.toGoatLatin("I speak goat Latin"))