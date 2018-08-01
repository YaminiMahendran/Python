class Solution(object):
    def checkRecord(self, s):
        count_a=0
        count_l=0
        s1=len(s)-1
        for i,each in enumerate(s):
            if(each=='A'):
                count_a +=1
            elif(i !=s1):
                if(each=='L' and s[i+1:i+3]=='LL' ):
                    count_l +=1
            else:
                pass
        if(count_a >=2 or count_l >=1):
            return False
        else:
            return True
        
        
        
s=Solution()
print(s.checkRecord("PPALLL"))