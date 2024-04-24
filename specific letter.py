'''m=input("enter string:")
for i in m.split():
    if 's' in  i.lower():
        print(i,end='  ')'''
        
o=input('enter string:').split()
a=[i for i in o if 's' in i]
print(str(a))