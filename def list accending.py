def list_assending():
    a = [2,3,8,4,6,8,8]
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] <= a[j]:
                a[i],a[j] = a[j],a[i]
    print(a)
list_assending()

