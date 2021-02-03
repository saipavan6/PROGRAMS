#using while loop
number = int(input("enter a number"))
start = 2
while start < number :
    if number % start == 0 :
        print("not a prime number")
        break
    start += 1

else :
    print("prime number")

#using for loop
number = int(input("enter a number"))
for start in range (2,number):
    if number % start == 0:
        print ('not prime')
        break
else :
    print('prime')



