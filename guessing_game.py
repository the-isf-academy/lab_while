######################
# Unit 0 Lab 5
# guessing_game.py
#######################

from random import randint

print("----------------------------")
print("Guess a number between 1-10!")
print("----------------------------\n")

game_won = False
number = randint(1,10)

while True:
    user_guess = int(input("Guess a number: "))

    if user_guess == number:
        print("Correct")
        game_won = True

