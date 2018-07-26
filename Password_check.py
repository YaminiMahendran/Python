#Password check
def password_check(new,old):
    count=0
    if(new!=old):
        for letter in new:
            count +=1
        if(count>=6):
            return True
        else:
            return False
    else:
        return False

print(password_check('E10-s2ff', 'E10.s2ff'))
    
        
    
