class Solution(object):
    def toGoatLatin(self, S):
        words=[]
        new_word=[]
        final=""
        words=S.split(" ")
        for each in words:
            if(each[0] == 'a' or each[0] =='e' or each[0] =='i' or each[0] =='o' or each[0] =='u' or each[0] == 'A' or each[0] =='E' or each[0] =='I' or each[0] =='O' or each[0] =='U'):
                new_word.append(each + 'ma')
            else:
                new_word.append(each[1:] +each[0]+'ma')
        print (new_word)
        i=1
        for i,word in enumerate(new_word):
            final += word + 'a' * (i+1) +' '
        final=final.rstrip()
        return final

s=Solution()
print(s.toGoatLatin("I love goat latin"))