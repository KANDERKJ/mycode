farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
# CODE CUSTOMIZATION 01 - Create a for-loop that displays the following data structure. How the data is displayed is up to you!


# EASY(ish):
#• Write a for loop that returns all the animals from the NE Farm!

# MEDIUM:
#• Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on that farm.

# HARD:
#• Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on that farm.

#• ...but only return ANIMALS from that particular farm.


print("Here at the NE Farm, we have the following animals:")
for every_animal in farms[0]["agriculture"]:
    print(every_animal) # print(every_animal, end=" ") will print horizontally

# simplest thing would be three different for loops (one hard coded to each farm) which are selected by if/elif
dude = input()
for dude in farms[0]["agriculture"]:
    if dude in
    print()
    elif due not in

for dude in farms[1]["agriculture"]:
    if dude in
    print()
    elif dude in

for dude in farms[2]["agriculture"]:
    if dude in
    print()
    else:

