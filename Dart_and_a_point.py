#Checking if the given point is inside a dart
import math
x=eval(input("Enter the X value (between -10 and 10) :"))
y=eval(input("Enter the Y value (between -10 and 10) :"))
r=8
#Function to calculate distance
def dart(x,y):
    value_1 = abs(x-0) ** 2 
    value_2 = abs(y-0) ** 2
    rad_dart = math.sqrt(value_1 + value_2)
    return rad_dart

rad_dart = dart(x,y)
#Function to calculate area of a circle
def area_circle(r,rad_dart):
    area_of_dart = math.pi * (rad_dart ** 2)
    area_of_circle = math.pi * (r ** 2)
    if(area_of_dart < area_of_circle):
        print ("It is in! ")
    else:
        print ("Point is outside")

area_circle(r,rad_dart)