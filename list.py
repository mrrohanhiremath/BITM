
'''apple[2]=(300,400)
print(apple)
print(apple[-1])
apple[3]=500,600,700
print(apple)
apple[1:4]=(-10,-20,-30)
print(apple)'''

college=[10,20,30,40,50,60,70,80,90,100]
print(college[1])
print(college[-1])
print(college[1:3])
print(college[1:7])
#print(college[7])
print(college[:])
print(college[3:-1])   #index value -1*-1=-2=40
print(college[-4:-1])
print(college[1:])
print(college[:-1])
print(college[0:])
print(college[0:4:3])

'''vaish=[]
n=int(input('enter the list size:'))
for i in range(0,n):
    ele=input('enter the elements:')
    vaish.append(ele)
print(vaish)'''

'''rohini=(10,20,30,40,50)
rohan=(60,70,80,90,100)
roshan=rohini+rohan                 #tuple() is immutable,it allows duplication
print(roshan)
print(type(rohini))
print(type(rohan))
print(roshan*2)
print(len(roshan))
print(min(roshan))
print(max(roshan))
print(sum(roshan))
print(list(roshan))'''

'''venus=[10,20,30]
mars=[40,50,60]
pluto=venus+mars
print(pluto)                          #list is varied length(dynamically allocated)
print(type(venus))                     []list is mutable
print(type(mars))                      it allows duplication
print(pluto*2)
print(len(pluto))
print(min(pluto))
print(max(pluto))
print(sum(pluto))
print(tuple(pluto))'''

'''pavi=[10,20,30,40,50]
sum=0
for i in pavi:      
    sum+=i         #if i%10==7:
print(sum)            # print(i)'''

'''sneha=[10,20,30,40,50,30,50]
humaira=[]
for i in sneha:
    if i not in humaira:
        humaira.append(i)
print(humaira)'''

'''yuva1=[10,20,30,40,50]
yuva2=[60,70,80,90,100,20]
for i in yuva1:
    for j in yuva2:
        if i==j:
            print(i)'''