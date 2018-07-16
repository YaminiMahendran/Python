def prime_no(number):
    counter=number
    count=0
    l=[]
    if(number==2):
        print (number,"is a Prime number")
    else:
        while(counter>=1):
            if(number%counter==0):
                count += 1
                l.append(counter)
                counter -= 1
            else:
                counter -= 1
        return count

no=eval(input("Enter a number to check if it's a Prime no:"))
count=(prime_no(no))
if(count==2):
    print ("Number is a prime number")
else:
    print("Number is not a prime number")