#!/usr/bin/env python3
import random

num= int(input("How many Shakespearean insults would you like?"))

insult_list= open("/home/student/mycode/friday_challenge/insult.txt", "r")

# it says insult list, but that's not a list, right? It needs converted into one.

insult= insult_list.readlines()


def insult_generator(num):
    print("You are a", end="")
    for x in range(num):
      print(random.choice(insult), end='')

insult_generator(num)
