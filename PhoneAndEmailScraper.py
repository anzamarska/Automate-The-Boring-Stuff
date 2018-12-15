#3! python3

import re, pyperclip

#TODO: Create a regex for phone numbers
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


#TODO: Create a regex for email adresses
EmailsRegex=re.compile(r'''
[a-zA-Z0-9.+_]+    #name part
@    #@symbol
[a-zA-Z0-9.+_]+    #2nd part

''',re.VERBOSE)

#TODO: Get the text off the clipboard

text=pyperclip.paste()

#TODO: Extract the email/phone fron this list

numbers=PhoneNumberRegex.findall(text)
emails=EmailsRegex.findall(text)
allPhoneNumbers=[]
for PhoneNumber in numbers:
    allPhoneNumbers.append(PhoneNumber[0])


print(allPhoneNumbers, emails)
#TODO: Copy the extract email/phone to the clipboard

results="\n".join(allPhoneNumbers) + "\n" + "\n".join(emails)
pyperclip.copy(results)

