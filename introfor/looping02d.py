#!/usr/bin/env python3

# dnsservers.txt = original file with lines contain .org's and .com's

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile: #open the exisiting file of servers(dnsserveers.txt) and reading    them off into the dnsfile variable
    # indent to keep the dnsfile object open
    # loop across the lines in the file
    for svr in dnsfile:
        svr = svr.rstrip('\n') # remove newline char if exists 
                               # would exists on all but last line
        # IF the string svr ends with 'org'
        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile: # open org-domain.txt and append the lines of srvfile
                srvfile.write(svr + "\n")
        # ELSE-IF the string svr ends with 'com'
        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
# no need to close our file - closed automatically



# 1st if takes the variable svrfile and writes the lines in svr into the file org-domain.txt
# 2nd elif takes the variable svrfile and writes the lines in svr into the file com-domain.txt

# data changes all the time! data is typically not stored inside python scripts.
# python reads fastest through dictionaries, most data is stored in spreadsheet
# spreadsheet is actually just a dictionary
