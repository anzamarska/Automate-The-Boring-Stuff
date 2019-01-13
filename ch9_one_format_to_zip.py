import os, zipfile, re

def backuptoZip(folder):
    folder = os.path.abspath(folder)

    number =1
    while True:
        zipFilename = os.path.basename(folder) + "_" +str(number) +".zip"
        if not os.path.exists(zipFilename):
            break
        number=number+1

    print("Creating %s" %(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, "w")


    for foldername, subfolders, filenames in os.walk(folder):
        backupZip.write(foldername)
        for filename in filenames:
            if filename.endswith('.txt'):
                newBase = os.path.basename(folder) + '_'
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue
                backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print ("Done")
    
  



backuptoZip("C:\\Users\\ANIA\\Desktop\\automate the boring stuff")
    
