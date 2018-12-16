import re

urlRegex=re.compile(r"http://[\S]+|https://[\S]+")
text=input("Write a text in which you want to find some url")

print(urlRegex.findall(text))


