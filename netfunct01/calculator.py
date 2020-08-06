#! /usr/bin/env python3


def add(cash, money):
    return  cash + money

def sub(cash, money):
    return cash - money

def mult(cash, money):
    return cash * money

def div(cash, money):
    return cash / money

print("Select below:\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n")
message = int(input("What would you like to do? 1, 2, 3, ,4 :"))
int1= float(input("Choose a number: "))
int2= float(input("Choose a second number: "))

if message == 1:
    print(int1 + int2)
elif message == 2:
    print(int1 - int2)
elif message == 3:
    print(int1 * int2)
elif message == 4:
    print(int1 / int2)
else:
    print("Invalid")

    
