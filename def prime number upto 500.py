def prime():
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
prime()
