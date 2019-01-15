import re

text = open("ch8_mad_libs.txt", "w")


input1=str(input("Enter a adjective"))

text=re.sub(r'ADJECTIVE',input1, text)

text.close()
