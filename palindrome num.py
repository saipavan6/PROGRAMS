number = int(input("enter a number"))
original_value = number
reverse_number = 0
while number > 0:
    first_value = number % 10
    reverse_number =  first_value + reverse_number * 10
    number = number //10
print(original_value,reverse_number)
if original_value == reverse_number :
    print('palindrome number')
else :
    print("not a palindrome")
