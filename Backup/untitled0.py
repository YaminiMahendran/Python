count = 0
while True:
    count += 1
    # end loop if count greater than 10
    if count > 10:
       break
    # skip 5
    if count == 5:
        continue
    print(count)
    
input("\n\nPress the enter key to exit.") 

import random
mylist = [10, 20, 30]
random.shuffle(mylist)
print(mylist)