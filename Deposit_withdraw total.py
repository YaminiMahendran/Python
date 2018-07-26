def statement(a):
    deposit=0
    withdraw=0
    for number in a:
        if(number>0):
         deposit += number
        else:
            withdraw += number
    return deposit,withdraw

print(statement([30.95, -15.67, 45.56, -55.00, 43.78]))
    