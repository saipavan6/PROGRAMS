a = [5,6,1,6,8,7]
def list_min():
    b= a[0]
    for i in a:
        if a[0] > i:
            if b > i:
                b = i
    print(b)
list_min()
