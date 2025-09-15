def fun():
    a=[]
    n=int(input('Enter the number of elements u r going to enter in an order:'))
    print('Enter the elements one by one:')
    for i in range (0,n):
        t=int(input())
        a.append(t)
    b=int(input('Enter the number u want to check for:'))
    for i in range(0,n):
        if b==a[i]:
            return 1
    return 0
print(fun())
