x1=eval(input("Enter X1:"))
y1=eval(input("Enter Y1:"))
x2=eval(input("Enter X2:"))
y2=eval(input("Enter Y2:"))
x=eval(input("Enter X:"))
y=eval(input("Enter Y:"))


#function to find other co-ordinates
def coordinates(x1,y1,x2,y2):
    print ("Co-ordinate 1(x1,y1):"+ str(x1),str(y1) )
    print ("Co-ordinate 2(x2,y2):"+ str(x2),str(y2) )
    print ("Co-ordinate 3(x2,y1):"+ str(x2),str(y1) )
    print ("Co-ordinate 4(x1,y2):"+ str(x1),str(y2) )

#Fuctions to calculate area of each triangle
def triangle1(x1,y1,x2,x,y):
    base= x2 - x1
    height= y - y1
    area_1=0.5 * abs(base) * abs(height)
    return area_1

def triangle2(y1,y2,x2,x,y):
    base= y2 - y1
    height= x2 - x
    area_2=0.5 * abs(base) * abs(height)
    return area_2

def triangle3(x1,y2,x2,x,y):
    base= x2 - x1
    height= y2- y
    area_3=0.5 * abs(base) * abs(height)
    return area_3
    
def triangle4(x1,y2,y1,x):
    base = y2 - y1
    height= x- x1
    area_4= 0.5 * abs(base) * abs(height)
    return area_4

#Calculating sum of all triangles
def sum_of_triangles(area_1,area_2,area_3,area_4):
    total= float(area_1) + float(area_2) + float(area_3) + float(area_4)
    return total
    
#Calculating area of a rectangle
def area_of_rect(x1,y1,x2,y2):
    length = x2 - x1
    breadth = y2 - y1
    area_rect=length * breadth
    return area_rect

#Calculating if the given point is inside a rectangle
def in_out(sum_tri,area_rect,area_1,area_2,area_3,area_4):
    if(sum_tri > area_rect):
        print("Point is outside Rectangle")
        return False
    else:
        print("Point is inside or on Rectangle")
        return True
    
#Invoking Functions
coordinates(x1,y1,x2,y2)
area_1=(triangle1(x1,y1,x2,x,y))
area_2=(triangle2(y1,y2,x2,x,y))
area_3=(triangle3(x1,y2,x2,x,y))
area_4=(triangle4(x1,y2,y1,x))
print("Area of Triangle_1:"+ str(area_1))
print("Area of Triangle_2:"+ str(area_2))
print("Area of Triangle_3:"+ str(area_3))
print("Area of Triangle_4:"+ str(area_4))
sum_tri=(sum_of_triangles(area_1,area_2,area_3,area_4))
print("Sum of Triangles:"+ str(sum_tri))
area_rect=(area_of_rect(x1,y1,x2,y2))
print("Area of Rectangle:"+ str(area_rect))
print(in_out(sum_tri,area_rect,area_1,area_2,area_3,area_4))