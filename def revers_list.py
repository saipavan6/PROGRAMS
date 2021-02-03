def revers_list(a,b):
    count = len(a) -1
    while count >= 0:
        b.append(a[count])
        count -= 1
    print(b)
a = [1,2,3,4,5,6,7]
b =[]
revers_list(a,b)
