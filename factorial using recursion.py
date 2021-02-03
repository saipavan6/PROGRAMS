def recursive(number,total):
        total = total *number
        if number == 1:
            print(total)
            return total
        number = number -1
        recursive(number,total)

        

number = int(input('enter a number'))
total = 1
recursive(number,total)
