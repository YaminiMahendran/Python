#Approximation of Pi square value

def approxPIsquared(float_err):
    prev_sum = 0
    current_sum = 0
    denominator = 1
    x=8
    while(current_sum - prev_sum != float_err):
        current_sum = prev_sum + ( x/(denominator ** 2))
        prev_sum = current_sum
        denominator = denominator + 2
    return current_sum
    
print(approxPIsquared(0.0001))
        
