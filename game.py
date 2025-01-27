#the Python guessing game code

#"As a tree you came, don't become charcoal; Be a ripe fruit, don't be unripe."
#HOUSHANG_EBTEHAJ

import random

while True:
    # Get the game level from the user
    try:
        level = int(input("Level: "))
    except ValueError:
         # Continue the loop if the user does not enter a valid integer
        continue
    # Check if the game level is positive
    if level <= 0:
        # Continue the loop if the game level is negative or zero
        continue
    # Generate a random number between 1 and the game level
    num = random.randint(1, level)
    # Break the loop after the random number is generated
    break

while True:
    # Get the user's guess
    try:
        guess = int(input("Guess: "))
        # Check if the user's guess is positive
        if guess <= 0:
            # Continue the loop if the user's guess is negative or zero
            continue
    except ValueError:
        # Continue the loop if the user does not enter a valid integer
        continue
    # Compare the user's guess to the random number
    if guess < num:
        print("Too small!")
    elif  guess > num:
        print("Too large!")
    else:
        print("just right!")
        # Break the loop if the guess is correct
        break
    #######################################################################################
#This code uses a while True loop to repeat the game steps until the user guesses the correct number.
#try-except is used to check the validity of the user's input and prevent errors.
#random.randint is used to generate a random number between 1 and the game level.
#Comparison operators (<, >, ==) are used to compare the user's guess to the random number.
