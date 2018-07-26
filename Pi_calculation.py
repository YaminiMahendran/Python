def approxPIsquared(input_float_error):
    prev_sum = 0
    current_sum = 0
    denominator = 1
    while(True):
        current_sum = prev_sum + 8/(pow(denominator ,2))
        if current_sum - prev_sum < input_float_error:
            break
        prev_sum = current_sum
        denominator = denominator + 2
    return current_sum
print(approxPIsquared(0.0001))
        