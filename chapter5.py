inventory={
    'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']



def displayInventory():
    tk=0
    for v, k in inventory.items():
        print (str(k) + " " + v)
        tk=tk+k
    print ("Total number of inventory items: " + str(tk))
    print("Total number of items: " + (str((tk)+len(dragonLoot))))


def addToInventory(inventory, addedItems):
    for item in dragonLoot:
        inventory.setdefault(item, 0)
        inventory[item]=inventory[item]+1
        

inv=addToInventory(inventory, dragonLoot)

displayInventory()






