#!/usr/bin/env python3
## create file object in "r"ead mode

filename= input("What file in the cfgread directory do you want to view?")
with open(filename, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
      
        
## file was just auto closed (no more indenting)

## display list with no "\n"
print(configlist)

length= len(configlist)
print(length)


    
