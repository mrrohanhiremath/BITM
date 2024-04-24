'''if(5>10):
    print("yes")
else:
    print("no")'''
'''age1=int(input('enter age1='))
age2=int(input('enter age2='))
if(age1>age2):
    age3=age1+age2
    print('my age added',age3)
else:
    age3=age1-age2
    print('my age subtracted',age)'''
'''email="vaishu@gmail.com"
pwd=909921
uemail=str(input("enter the email"))
upwd=int(input("enter the password"))
if(email==uemail and pwd==upwd):
    print("login success")
else:
    print("login failed")'''
    
email="vaish@gmail.com"
pwd=123456
otp=909921
uemail=str(input("enter the email"))
upwd=int(input("enter the pwd"))
uotp=int(input("enter the otp"))
if(email==uemail):
    if(pwd==upwd):
        if(otp==uotp):
            print("transaction successful")
        else:
            print("transaction failed due to incorrect otp")
    else:
        print("transaction failed due t0 incorrect pwd")
else:
    print("transaction declined")

'''#a=-5
#print(abs(a))
#print(pow(2,3))'''

'''num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
if(num1>num2):
    print(num1,"num1 is greater")
elif(num1==num2):
   print("num1 is equal to num2")
else:
    print(num2,"num2 is greater")'''


num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
num3=int(input("enter the num3:"))
print( "num1" if (num1>num2 and num1>num3) else "num2" if(num2>num3) else "num3")
    