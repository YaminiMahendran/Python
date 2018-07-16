def counting_string(str1):
    c1=0
    c2=0
    c3=0
    for letter in str1:
        if(letter.isalpha()):
            c1 += 1
        elif(letter.isnumeric()):
            c2 += 1
        elif(letter == " "):
            c3  += 1
        else:
            print ("Not a character/Number/Space")
    return c1,c2,c3
s1=(input("Enter a String:"))
print ("Characters,Numeric,Spaces count:",counting_string(s1))