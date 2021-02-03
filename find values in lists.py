
lists = [ 1,2,3,4,5,6,7,8,9,10 ]
number = int(input('enter a finding value in the list '))
for i in lists :
    if i == number :
        print(' yes matching')
        break

else:
        print(number, 'not finding in list')
"""

lists = [ 1,2,3,4,5,6,7,8,9,10 ]
number = int(input('enter a finding value in the list '))
count = 0
while len(lists) > count:
    if  lists[count] == number :
        print("yes")
        break
    count += 1
else :
    print('no')
"""
