class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse=[]
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        morse_code={}
        new_list=[]
        transform_list=[]
        counter=0
        transform={}
        final=[]
        morse_code = dict(zip(alpha,morse))
        for word in words:
            new_list=[]
            for letter in word:
                if(letter in morse_code.keys()):
                    new_list.append(morse_code[letter])
            transform[counter]= new_list
            counter +=1 
            transform_list=transform.values()
        #print transform_list
        final=[]
        final1=set()
        for each in transform_list:
            one=''
            for letter in each:
                one += (letter)
            final.append(one)
        print (final)
        final1=set(final)
        return len(final1)
    
"""        loopnum = 0
word = 'afrykanerskojęzyczny'
wordlist = ['afrykanerskojęzycznym','afrykanerskojęzyczni','nieafrykanerskojęzyczni']
for i in wordlist:
    wordlist[loopnum] = word
    loopnum += 1
"""

s=Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))