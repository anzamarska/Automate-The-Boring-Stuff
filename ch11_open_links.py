import webbrowser, re

text = open("ch11_text_with_links.txt", "r")
ntext=text.readlines()
ntext=str(ntext)
text.close()

print(ntext)

link = re.compile(r'https://[^\s]+')
mo = link.findall(ntext)
print (mo)

for eachlink in mo:
    webbrowser.open(eachlink)

