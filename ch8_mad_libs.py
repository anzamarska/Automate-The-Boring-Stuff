import re

text = open("ch8_mad_libs.txt", "w")

content = text.read()

adj=re.compile(r'ADJECTIVE')

input1=str(input("Enter a adjective"))


text=adj.sub(input1, text)

text.write(text)


text.close()
