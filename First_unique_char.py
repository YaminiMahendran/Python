class Solution(object):
    def firstUniqChar(self, s):
        new=[]
        first_element=[]
        char_set=[]
        unique=''
        for i,each in enumerate(s):
            first_element.append(s.count(s[i]))
        print (first_element)
        for i,each in enumerate(first_element):
            if each==1:
                char_set.append(s[i])
            else:
                new.append(s[i])
        #print (char_set)
        unique=char_set[0]
        if unique in s:
            return (s.find(char_set[0]))
        else:
            return (-1)
                

s=Solution()
print(s.firstUniqChar("popcorn"))