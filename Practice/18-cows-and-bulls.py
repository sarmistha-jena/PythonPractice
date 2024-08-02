# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
# For every digit that the user guessed correctly in the correct place, they have a “cow”. 
# For every digit the user guessed correctly in the wrong place is a “bull.” 
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
# Once the user guesses the correct number, the game is over. 
# Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

import random

def cows_and_bulls():
    random_number = str(random.randint(1000, 9999))
    guesses = 0

    while True:
        user_guess = input("Guess a 4 digit number : ")
        guesses += 1
        cows = 0
        bulls = 0
        for i in range(4):
            if user_guess[i] == random_number[i]:
                cows += 1
            elif user_guess[i] in random_number:
                bulls += 1

        print(f"{cows} cows, {bulls} bulls")
        if cows == 4:
            print(f"You guessed the number in {guesses} guesses!")
            break
        else:
            print("Try again.")
            continue

if __name__ == "__main__":
    print("Welcome to the Cows and Bulls Game!")
    cows_and_bulls()
    print("Thanks for playing!")