#Reading the input file
import random
txt={}
with open('D:\words.txt','r') as infile:
    for line in infile:
        (key,val) = line.split(':')
        txt[key] = val
 
jumbled_word=""
scrambled_word=[]
words=list(txt.keys())
meaning=txt.values()
jumbled=""
word=""

#Function to scramble a word
def jumbled_word(w):
    temp=list(w)
    random.shuffle(temp)
    jumbled="".join(temp)
    return jumbled 

#Function to pull the meaning of a scrambled word
def meaning(w):
    meaning=txt[w]
    return meaning

print("Unscramble the letters to form a word.")
print("Type '?' for the meaning of the unscrambled word")
while True:
    word=random.choice(words)
    jumbled = jumbled_word(word)
    mean =meaning(word)
    print(jumbled)
    response=input("Enter word [? for meaning of unscrambled word]: ")
    if(response.lower() == word):
        response1=input("You got it! Do you want to continue [yes or no]:" )
        if(response1.lower() =='yes'):
            continue
        else:
            break
    elif(response == "?"):
        print("The word means:",mean)
        response=input("Enter word : ")
        if(response.lower()==word):
            response1=input("You got it! Do you want to continue [yes or no]:" )
            if(response1.lower() == 'yes'):
                continue
            else:
                break
    else:
        break




    