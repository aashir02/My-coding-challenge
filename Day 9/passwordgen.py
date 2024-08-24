import string

req=[]
lower=list(string.ascii_lowercase)
upper=list(string.ascii_uppercase)
digits=list(string.digits)
special_char=list(string.punctuation)

print("Welcome to THE PASSWORD GENERATOR!!!")
len=int(input("Enter the length for the passsword: "))
for i in range(4):
    low=input("Do you want lower case letters in your password (y/n): ")
    if low=='y':
        req.append(True)
    else:
        req.append(False) 

    upp=input("Do you want upper case letters in your password (y/n): ")
    if upp=='y':
        req.append(True)
    else:
        req.append(False)

    digit=input("Do you want digits in your password (y/n): ")
    if digit=='y':
        req.append(True)
    else:
        req.append(False)

    spl_char=input("Do you want special characters in your password (y/n): ")
    if spl_char=='y':
        req.append(True)
    else:
        req.append(False)
    break

print(req[0])
              