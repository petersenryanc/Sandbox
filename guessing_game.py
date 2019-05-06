"""
Guess the number game. Program tells user if guess is too high or too low.
Credit: Talk Python (training.talkpython.com)
"""

import random
print("---------------------")
print("  GUESS THE NUMBER")
print("---------------------")

the_number = random.randint(0, 100)
guess = -1


while guess != the_number:
    guess = int(input("Guess a number between 0 and 100: "))
    if guess < the_number:
        print("{} is too low!".format(guess))
    elif guess > the_number:
        print("{} is too high!".format(guess))
    else:
        print("{} is correct! You win!".format(guess))
print("Goodbye")
