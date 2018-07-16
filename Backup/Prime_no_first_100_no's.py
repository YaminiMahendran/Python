def prime_no(number):
    counter=number
    count=0
    if(number==2):
        return 2,2
    else:
        while(counter>=1):
            if(number%counter==0):
                count += 1
                counter -= 1
            else:
                counter -= 1
        return count,number

no=eval(input("Enter a number to check if it's a Prime no:"))
l=[]
while(no >=1):
    count,number=(prime_no(no))
    if(count==2):
        l.append(number)
        no -= 1
    else:
        no -= 1
print(l)