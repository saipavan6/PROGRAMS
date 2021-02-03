number = int(input("enter a number"))
reverse_number = 0
while number > 0:
    first_value = number % 10
    reverse_number =  first_value + reverse_number * 10
    number = number //10
print(reverse_number)
