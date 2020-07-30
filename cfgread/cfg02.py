#!/usr/bin/env python3

user_input = input("What file would you like to load?")
count = 0
## create file object in "r"ead mode
configfile = open(user_input, "r")

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no "\n"
print(configlist)

for elements in configlist:
    count= count + 1
    print(count)
# Always close your file
configfile.close()


