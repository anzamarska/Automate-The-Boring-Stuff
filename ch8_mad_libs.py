import re

file = open("ch8_mad_libs.txt", "w")

adj=re.compile(r'ADJECTIVE')

input1=str(input("Enter a adjective"))
fileStr=str(file)

fileStr=adj.sub(input1, fileStr)

file.write(fileStr)


file.close()
