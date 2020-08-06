#!/usr/bin/env python3    
def main():
    x= float(input("How would you rank your day today on a scale of 1-10?"))
    if x == 10:
        print("Attaboy! Stay positive!")
    elif x >= 8:
        print("Sounds lovely! Keep on truckin'!")
    elif x >= 6:
        print("Chin up, buttercup!")
    elif x >= 4:
        print("I recommend some hot chocolate and a hug, maybe...")
    elif x >= 2:
        print("Dude, are you ok?")
    else:
        print("Geez!!! You might as well just go back to bed!")
main()
