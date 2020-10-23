# This program will roll one D4, D6, D8, D10, D12, or D20 die
# If you don't know what these dice are for, ask your nearest nerd friend
# Instructions used for Random module: https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/
# Validation tips from: https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response

# Import random module
from random import randint

#Ask for dice type and validate response
while True:
    dice_type = input("Which die would you like to roll? \
        Choose D4, D6, D8, D10, D12, or D20: ")
    if dice_type.upper() not in ('D4', 'D6', 'D8', 'D10', 'D12', 'D20'):
        print("Please select an appropriate die from the list")
    else:
        break

#Set choice to uppercase
dice_type = dice_type.upper()

# Print the selected die
print("You chose:",dice_type)

# Calculate random number depending on dice_type
# randint accepts (start, end) as parameters and generates a random integer between the two
# Use IFs to determine the random number range
# Python doesn't have CASE statements so I don't know how to do this neatly
if dice_type == "D4":
    dice_roll = randint(1,4)
    print("You rolled:", dice_roll)
elif dice_type == "D6":
    dice_roll = randint(1,6)
    print("You rolled:",dice_roll)
elif dice_type == "D8":
    dice_roll = randint(1,8)
    print("You rolled:",dice_roll)
elif dice_type == "D10":
    dice_roll = randint(1,10)
    print("You rolled:",dice_roll)
elif dice_type == "D12":
    dice_roll = randint(1,12)
    print("You rolled:",dice_roll)
elif dice_type == "D20":
    dice_roll = randint(1,20)
    print("You rolled:",dice_roll)
else:
    print("Oh no your dice fell off the table!")
