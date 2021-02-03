def hello():
    global ages
    ages = 100
    print('local namespace',100)
ages = 30
print('global',ages)
hello()
print('after fuction call',ages)
