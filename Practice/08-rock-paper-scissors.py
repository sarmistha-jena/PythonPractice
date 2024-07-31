# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of 
# congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock
def playgame():
    userinput1 = input("User1!! Please enter your choice: ").lower()

    userinput2 = input("User2!! Please enter your choice: ").lower()

    if userinput1 == "rock" and userinput2 == "scissors":
        print("User1 wins")
    elif userinput1 == "scissors" and userinput2 == "paper":
        print("User1 wins")
    elif userinput1 == "paper" and userinput2 == "rock":
        print("User1 wins")
    elif userinput1 == userinput2:
        print("It's a tie")
    else:
        print("User2 wins")
    playagain = input("Do you want to play again? Y or N ")
    if playagain.lower() == "y":
        playgame()
    else:
        print("Thank you for playing")

print("Welcome to Rock-Paper-Scissors game")
playgame()
