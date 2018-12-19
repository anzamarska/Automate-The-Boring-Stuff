tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


colWidths={"1colWidths":0,"2colWidths":0,"3colWidths":0}
x=4                     #how many elem are in list in list

a=-1
b=0
for k in colWidths:
    v=colWidths[k]
    while a < x-1:
        a=a+1
        while len(tableData[b][a]) > v:
            v=len(tableData[b][a]) #assigning the value of the longest word from the internal list to the width of the column
            colWidths[k]=v
    if a == x-1:
        b=b+1
        a=-1
            
        
        
print(colWidths)

def printTable():
    a=0
    b=0
    print (tableData[b][a].rjust(colWidths["1colWidths"]), tableData[b+1][a].rjust(colWidths["2colWidths"]), tableData[b+2][a].rjust(colWidths["3colWidths"]))
    print (tableData[b][a+1].rjust(colWidths["1colWidths"]), tableData[b+1][a+1].rjust(colWidths["2colWidths"]), tableData[b+2][a+1].rjust(colWidths["3colWidths"]))
    print (tableData[b][a+2].rjust(colWidths["1colWidths"]), tableData[b+1][a+2].rjust(colWidths["2colWidths"]), tableData[b+2][a+2].rjust(colWidths["3colWidths"]))
    print (tableData[b][a+3].rjust(colWidths["1colWidths"]), tableData[b+1][a+3].rjust(colWidths["2colWidths"]), tableData[b+2][a+3].rjust(colWidths["3colWidths"]))
    
printTable()
