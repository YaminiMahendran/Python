"""
def front3(my_str):
    new_str =""
    for letter in my_str[0:3]:
        new_str =new_str+letter
    return new_str * 3
"""

def front3(my_str):
    new_str =""
    count=1
    for letter in my_str:
        if(count <=3):
            new_str =new_str+letter
            count += 1
    return new_str * 3        

my_str =input("Enter a string:")
print(front3(my_str))
