stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory():
    x=0
    total=0
    while x < len(stuff):
        for k,v in stuff.items():
            total=total+v
            x=x+1
    print (total)
        
    print("Inventory:\n")
    for k, v in stuff.items():
        print(str(v) + " " + k)
    print("Total number of items: " + str(total))


displayInventory()

