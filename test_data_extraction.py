#! python3
import PhoneAndEmailScraper, re, pyperclip

text=pyperclip.paste()

findPhoneNumbers(text)
findEmail(text)

