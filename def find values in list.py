given_list = [1,2,3,4,5,6]
def find_values_in_list(finding_number):
    for i in given_list:
        if i == finding_number :
            print('YES , given value in a list at index{}'.format(i))
            break
    else:
            print('given value not in list')
finding_number = int(input('enter searching value in list:'))
find_values_in_list(finding_number)
