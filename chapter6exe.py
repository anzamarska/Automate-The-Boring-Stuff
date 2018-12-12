picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

def printPicnic(dictionary, leftWidth, rightWidth):
    print ("PICNIC ITEMS".center (leftWidth+rightWidth, "*"))
    for k, v in dictionary.items():
        print (k.ljust(leftWidth) + str(v).rjust(rightWidth))

printPicnic (picnicItems, 8, 10)
