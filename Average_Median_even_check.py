#Reads a list of number
my_list=input("Enter a list of integers:").split(" ")
length=len(my_list)
my_list.sort()
avg=0
temp=0
m1=0
m2=0
sum=0
middle=0
#Function to calculate average
def average(my_list):
    total=0
    for number in my_list:
        total =total+ int(number)
    avg=total/length
    return avg
#Fuction to calculate  median
def median(my_list):
    if(length%2==0):
        temp=int(length)//2
        m1=my_list[temp]
        m2=my_list[temp-1]
        sum=int(m1)+int(m2)
        middle=sum/2
        return middle
    else:
        temp=int(length)//2
        m1=my_list[temp]
    return m1
#Function to calculate count of even numbers in the list
def even_no(my_list):
    count=0
    for no in my_list:
        if(int(no)%2 == 0):
            count += 1
    return count
print("Average of Integers in the list is :"+ str(average(my_list)))
print("Number of even numbers in the list is :"+ str(even_no(my_list)))
print ("Median of numbers in the list is :" + str(median(my_list)))    
        






