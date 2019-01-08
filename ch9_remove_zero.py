import shutil, os, re

zero = re.compile(r'''^(.*?)
(0{2,})
(.*?)$
''', re.VERBOSE)

for oldFileName in os.listdir('.'):
    mo = zero.search(oldFileName)
    if mo == None:
        continue
    beforePart = mo.group(1)
    zerosPart = mo.group(2)
    afterPart = mo.group(3)
    newName= beforePart + afterPart

    absWorkingDir= os.path.abspath('.')
    oldFileName=os.path.join(absWorkingDir, oldFileName)
    newFileName=os.path.join(absWorkingDir, newName)
    
    print ('Renaming "%s" to "%s"...' % (oldFileName, newFileName))
    #shutil.move(oldFileName, newFileName)


