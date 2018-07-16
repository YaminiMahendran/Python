def nearest10(a,b):
    diff1= abs(a-10)
    diff2=abs(b-10)
    if(diff1 > diff2):
        return b 
    elif(diff1< diff2):
        return a
    else:
        return 0
       

a=int(input("Enter the first Value:"))
b=int(input("Enter the second value:"))
print(nearest10(a,b))