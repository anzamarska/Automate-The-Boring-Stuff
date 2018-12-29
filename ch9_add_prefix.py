#! python3
import os,re, shutil

for oldFilename in os.listdir('.'):
    newName = "spam_" + oldFilename
    absWorkingDir= os.path.abspath('.')
    newFilename = os.path.join(absWorkingDir, newName)

    print('Renaming "%s" to "%s"' % (absWorkingDir + "\\"+ oldFilename, newFilename))
    #shutil.move(absWorkingDir + "\\"+ oldFilename, newFilename)
