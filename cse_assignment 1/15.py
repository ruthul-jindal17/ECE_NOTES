list1=[]
c=0
a=int(input("Enter the number of elements in the list:"))
print('Enter the elements of the list one by one:')
for i in range(0,a):
    ele=str(input())
    list1.append(ele)
for i in range(0,a):
    strng=list1[i]
    k=len(strng)
    if strng[0]==strng[k-1]:
        c=c+1
print('the number of strings with first and last charecter eqaul:',c)
