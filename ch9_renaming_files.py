#! python3
import os,re, shutil

#    Create a regex that can identify the text pattern of American-style dates.

AmericanDataStyle = re.compile(r'''^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20) \d\d)
(.*?)$
''', re.VERBOSE)

#    Call os.listdir() to find all the files in the working directory.
#    Loop over each filename, using the regex to check whether it has a date.

for amerFilename in os.listdir('.'):
    mo = AmericanDataStyle.search(amerFilename)
    if mo == None:
        continue
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)


#    If it has a date, rename the file with shutil.move().

    EuroDataStyle = beforePart + dayPart+ "-" + monthPart + "-" + yearPart + afterPart
    absWorkingDir= os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, EuroDataStyle)

    print('Renaming "%s" to "%s"' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)


    
