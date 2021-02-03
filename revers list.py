lists = [1,2,3,4,5,6]
revers_list = []
lists_length = len(lists)-1
while lists_length >= 0:
    revers_list.append(lists[lists_length])
    lists_length -= 1
print(revers_list)
