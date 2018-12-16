import re

string=input("Please give a string")

beginningSpace=re.compile(r"^\s+")
string=beginningSpace.sub("",string)
endingSpace=re.compile(r"\s+$")
string=endingSpace.sub("",string)


print(string)
