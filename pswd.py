import re

def is_valid_pswd(pswd):
    if  (len(pswd)<=6 and len(pswd)>=16):
        return True
    if re.search("[a-z]",pswd):
        return True
    if re.search("[A-Z]",pswd):
        return True
    if re.search("[0-9]",pswd):
        return True
    if re.search("[$@#]",pswd):
        return True
    return False

pswd=input("enter the password:")
if is_valid_pswd(pswd):
    print("Valid password")
else:
    print("Invalid password")
    