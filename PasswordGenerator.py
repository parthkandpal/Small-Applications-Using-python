import random
import pyperclip
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%&_?'
nopass=int(input("enter the number of password you want to generate?"))

passLength=int(input("Password Length?"))

for p in range(nopass):
    password=''
    for c in range(passLength):
        password+=random.choice(chars)

    print(password)



