import random
print("---------------------")
print("  GUESS THE NUMBER")
print("---------------------")

the_number = random.randint(0, 100)
guess = -1


while guess != the_number:
    guess = int(input("Guess a number between 0 and 100: "))
    if guess < the_number:
        print("Too low!")
    elif guess > the_number:
        print("Too high!")
    else:
        print("You win!")
print("Goodbye")
