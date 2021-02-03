lists = [5,9,2,7,6,9,1]
for i in range(len(lists)):
    for j in range(len(lists)):
        if lists[i] > lists[j] :
            print(lists[i],lists[j])
            lists[i],lists[j] = lists[j],lists[i]
print(lists)
