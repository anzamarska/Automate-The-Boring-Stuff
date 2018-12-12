#! python3
# pw.py - An insecure password locker program.

passwords={"aaa":"hasloaaa",
           "bbb":"haslobbb",
           "ccc":"hasloccc"}
    

import sys, pyperclip
if len (sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

account=sys.argv[1] #first command line arg in the account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print("Password for" + account + "copied to clipboard")
else:
    print("There is no account named " + account)

