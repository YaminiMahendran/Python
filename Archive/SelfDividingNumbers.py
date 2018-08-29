class Solution(object):
    def selfDividingNumbers(self, left, right):
        org_list=[]
        for i in range(left,right+1):
            org_list.append(i)
        new=[]
        final1=set()
        final2=set()
        result=[]
        for element in org_list:
            new = [int(x) for x in str(element)]
            for e in new:
                if e !=0:
                    if element % e==0:
                        final1.add(element)
                    else:
                        final2.add(element)
                else:
                    final2.add(element) 
        result = list(final1 - final2)
        result=sorted(result)
        return result
        