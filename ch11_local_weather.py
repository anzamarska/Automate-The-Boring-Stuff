#!python3

import webbrowser,sys,pyperclip


if len(sys.argv) > 1:
    localization = ' '.join(sys.argv[1:])
else:
    localization = pyperclip.paste()
    
webbrowser.open("https://www.google.com/search?client=firefox-b-ab&q=pogoda+" + localization)
