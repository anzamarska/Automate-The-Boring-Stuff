def findEmail(text):
    return
    EmailsRegex=re.compile(r'''
    [a-zA-Z0-9.+_]+    #name part
    @    #@symbol
    [a-zA-Z0-9.+_]+    #2nd part

    ''',re.VERBOSE)

    emails=EmailsRegex.findall(text)

    print("\n".join(emails))

def test_answer():
    assert func('''When you run this program, the output will look something like this:

Copied to clipboard:
800-420-7240
415-863-9900
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
help@nostarch.com''') == info@nostarch.com
media@nostarch.com
academic@nostarch.com
help@nostarch.com
