import re

password=input("Please enter your password")
weak=0
mo1=[]


try:
    numberInPassword=re.compile(r"\d")
    monumber=numberInPassword.search(password)
    mo1.append(monumber.group())
except AttributeError:
    weak=weak+1

try:
    capitalLetterInPassword=re.compile(r"[A-Z]")
    mocapital=capitalLetterInPassword.search(password)
    mo1.append(mocapital.group())
except AttributeError:
    weak=weak+1

try:
    lowerLetterInPassword=re.compile(r"[a-z]")
    molower=lowerLetterInPassword.search(password)
    mo1.append(molower.group())
except AttributeError:
    weak=weak+1

try:
    numberOfLetters=re.compile(r"[a-zA-Z0-9]{8,}")
    numberOfLetters.search(password)
    mo1.append(monumber.group())
except AttributeError:
    weak=weak+1

                           

if weak !=0:
    print("Your password is too weak")
else:
    print("Your password is correct")
