
for number in range (2,501):
    for j in range (2,number):
        if number % j == 0 :
        
            break
    else:
        print(number, end = ',')

"""

count = 2

while count <= 500:
    yes = 0
    number = 2
    while count > number :
        if count % number == 0:
            yes = 1
            break
        number += 1
    if yes == 0 :
        print (count , end = ',')
        
    count += 1
"""
