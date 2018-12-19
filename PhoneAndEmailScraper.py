#3! python3

import re, pyperclip
text=pyperclip.paste()

def findEmail(text):
    
    EmailsRegex=re.compile(r'''
    [a-zA-Z0-9.+_]+    #name part
    @    #@symbol
    [a-zA-Z0-9.+_]+    #2nd part

    ''',re.VERBOSE)

    emails=EmailsRegex.findall(text)

    print("\n".join(emails))

def findPhoneNumbers(text):
    
    PhoneNumberRegex=re.compile(r'''
    (
    (\d{3})|(\(\d{3}\))?
    (-)?
    (\d{3})
    (-)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )
    ''', re.VERBOSE)

    numbers=PhoneNumberRegex.findall(text)

    allPhoneNumbers=[]
    for groups in PhoneNumberRegex.findall(text):
        phoneNum = ''.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        allPhoneNumbers.append(phoneNum)

    print("\n".join(allPhoneNumbers))

findEmail(text)
findPhoneNumbers(text)


