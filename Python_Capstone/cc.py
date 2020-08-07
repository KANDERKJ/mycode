#!usr/bin/env python3


# make a python currency converter

with open('currencyData.txt') as file:
    lines = file.readlines()
    currencyDict = {}
    for line in lines:
        parsed = line.split("\t")
        currencyDict[parsed[0]] = parsed[1]

print(" What is the name of the currency you want to convert from USD?\
        Options:")
[print(item) for item in currencyDict.keys()]

while True:
    try:
        currency = input("Please enter one of these values:\n")
        foreign_cash= float(currencyDict[currency])
        break
    except:
        print("That's not an acceptable currency. Try again.")
while True:
    try:
        amount = float(input("Enter amount:\n"))
        print(f'{amount} USD is equal to {amount * foreign_cash}\
        {currency}')
        break
    except:
        print("That not a real amount. Try again.")

