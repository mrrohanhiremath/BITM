2) Python Program to Print Largest Even and Largest Odd Number in a List

n=int(input("Enter the number of elements to be in the list:"))
b=[]
for i in range(0,n):
    a=int(input("Element: "))
    b.append(a)
c=[]
d=[]
for i in b:
    if(i%2==0):
        c.append(i)
    else:
        d.append(i)
c.sort()
d.sort()
count1=0
count2=0
for k in c:
    count1=count1+1
for j in d:
    count2=count2+1
print("Largest even number:",c[count1-1])
print("Largest odd number",d[count2-1])


