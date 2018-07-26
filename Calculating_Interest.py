year=0
p_amt= eval(input("Enter Principal Amount:"))
ann_interest= eval(input("Enter the Annual Interest Rate:"))
interest=ann_interest/100
while (p_amt  <= (2 * p_amt)):
    p_amt += interest
    year +=1
    continue
print (p_amt)
print (year)