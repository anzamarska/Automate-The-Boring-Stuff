import re

text = open("ch8_mad_libs.txt", "w")


input1=str(input("Enter a adjective"))

adj = re.compile(r"ADJECTIVE")
adj.sub("input1","text")


text.close()
