def findPhoneNumbers(text):
    return
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

    
def test_answer():
    assert func('''When you run this program, the output will look something like this:

Copied to clipboard:
800-420-7240
415-863-9900
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
help@nostarch.com''') == 800-420-7240
415-863-9900
415-863-9950
