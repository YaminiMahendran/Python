#Calculating Simple Interest
def calculateInterest(P_amt,interest_rate,years):
    interest_amt=0
    interest_amt=(P_amt * interest_rate * years) /100
    return interest_amt

print(calculateInterest(1000.00, 8.0, 10))


    
    
    
    