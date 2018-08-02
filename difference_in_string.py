class Solution(object):
    def findTheDifference(self, s, t):
        new=""
        s_dict={}
        t_dict={}
        for each in s:
            if each in t:
                s_dict[each] = s_dict.get(each,0) +1
        for each in t:
            if each in s:
                t_dict[each] = t_dict.get(each,0) +1
            else:
                new += each
        #print (t_dict,s_dict,new)
        for each in t_dict:
            if t_dict[each] !=s_dict[each]:
                new += each
        return (new)
        
        
s=Solution()
print(s.findTheDifference('abb','abbd'))