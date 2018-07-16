a =int(input("Enter 1st no:"))
b =int(input("Enter 2nd no:"))
c =int(input("Enter 3rd no:"))

def max_3(a,b,c):
    if(a >= b and a >= c):
        max = a
    elif(b >= a and b >= c):
        max = b
    else:
        max = c
    return max

print(max_3(a,b,c))

    