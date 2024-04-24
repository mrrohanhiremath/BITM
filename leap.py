def isleapyear(year):
    if(year % 4 == 0 and year % 100!=0):
        return True
    else:
        return False
    
year=int(input("enter a year:"))
if isleapyear (year):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")