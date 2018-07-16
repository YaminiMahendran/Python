a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
a_last= a %10 
b_last= b %10

def last_digit(a,b):
    if (a_last == b_last):
        return True
    else:
        return False
    
print(last_digit(a_last,b_last))