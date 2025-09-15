a=[1,4,9,16,25,36,49,64,81,100]
b=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        b.append(a[i])
for i in range(0,len(b)):
    print(b[i])
