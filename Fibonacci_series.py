def fibonacci(no):
    count=0
    l=[0,1]
    while(count<=no):
        sum=l[count]+l[count+1] #(0+1 =1) ,(1+1=2)
        l.append(sum) # [0,1,1,],[0,1,1,2]
        count +=1 #count=1
        no -=1 # 4
    return l   
print(fibonacci(10))
        