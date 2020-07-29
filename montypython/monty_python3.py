#!/usr/bin/python3
round = 0
answer = " "

while round < 3 and answer != "Brian":
    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    if answer == "Brian": # logic to check if user gave correct answer
        print("Correct!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!") 


# CODE CUSTOMIZATION 01 - Try to write the logic that would allow a user to provide a lowercase or uppercase answer, and still get credit. You should be able to come up with this solution based on what you've already learned.

# CODE CUSTOMIZATION 02 - If the user provides the string shrubbery as input, the script should print to the screen, You gave the super secret answer!, and exit.
