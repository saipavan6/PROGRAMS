#divisible by 20
number = int(input("enter a number :"))
if number < 20:
    print("please enter a  value greater than 20")
elif number %20 == 0:
    print(number, "is divisible by 20")
else:
    print(number , "not divisible by 20")
                   
