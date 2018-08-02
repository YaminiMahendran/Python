class Solution(object):
    def isAnagram(self,s,t):
        count =0
        counter=0
        print (s,t)
        s_dict={}
        t_dict={}
        for letter in s:
            if letter in t:
                count +=1
                s_dict[letter] =s_dict.get(letter,0) +1
        for letter in t:
            if letter in s:
                t_dict[letter]=t_dict.get(letter,0)+1
        print (s_dict,t_dict)
        for each in s_dict:
            if each in t_dict:
                if t_dict[each]== s_dict[each]:
                    counter += s_dict[each]
        print (counter)
            
        if (len(s)==len(t)) and (count ==len(t) and counter==len(t)):
            return True
        else:
            return False

s=Solution
print(s.isAnagram( "anagram" ,"accc","caac"))