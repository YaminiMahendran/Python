#Checking Palindrome of a String
x=input("Enter a String:")
y=x[::-1]
print (y) 
if(x==y):
    print("String is a Palindrome")
else:
    print("String is not a Palindrome")
