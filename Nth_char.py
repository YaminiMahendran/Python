my_str= input("Enter a string:")
char= int(input("Enter the nth character:"))
new_str=""
index=0
for letter in my_str:
    if(index%char==0):
        new_str += letter
        index +=1
    else:
        index +=1
print(new_str)

    
