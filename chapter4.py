spam = ['apples', 'bananas', 'tofu', 'cats']

def returnastring ():
    suma=1
    toprint= spam[0]
    while suma < len(spam):
        if suma < len(spam)-1:
            toprint= toprint + ", " + spam[suma] 
            suma= suma+1
        elif suma == len(spam)-1:
            toprint= toprint + " and " + spam[suma]
            suma= suma+1
    print (toprint)


returnastring()
