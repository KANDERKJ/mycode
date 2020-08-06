#!/usr/bin/env python3

# put that code in a function
# take the input string, set as variable
# figure out how to pass that string variable into the function

from random import choice

sentence = 'Hello World'

# tuple is a list that you can't change
# choice picks a random element from a list
# we are randomizing letters within the sentence
# 2 methods upper and lower of the strings
# join the empty string with c with choice of upper or lower method
# c is each character
# for loop is looping across the string which is every character in our variable sentence
print(''.join(choice((str.upper, str.lower))(c) for c in sentence))

# rewritten
for c in sentence:
    print(''.join(choice((str.upper, str.lower))(c)), end="")

# rewritten in a function
print()
def spongebob():
    for c in sentence:
        print(''.join(choice((str.upper, str.lower))(c)), end="")

spongebob()


# need to define our modules before we use them! do imports first!
# define a block of code(called a function) that we can call on at any time. Try to put these at the top of your scripts!
# if your function is going to use an outside variable( any variable not set inside of the function itself), then define that BEFORE you use that function.

# call on the function if:
#  1. the function has been defined
#  2. all the variables have been defined
