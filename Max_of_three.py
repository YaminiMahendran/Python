import math
x= eval(input("Enter the value of x:"))
y= eval(input("Enter the value of y:"))
z= eval(input("Enter the value of z:"))
avg=0
big=0
def average(x,y,z):
    avg=(x)+(y)+(z)/3
    return avg
def maximum(x,y,z):
    big=x
    if (y > big):
        big=y
        return big
    elif(z > big):
        big=z
        return big
print ("Average of three numbers is :",average(x,y,z))
print ("Maximum of three numbers is :",maximum(x,y,z))
