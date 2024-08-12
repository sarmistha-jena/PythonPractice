# In the game of Hangman, a clue word is given by the program that the player has to guess, 
# letter by letter. The player guesses one letter at a time until the entire word has been guessed. 
# (In the actual game, the player can only guess 6 letters incorrectly before losing).

# Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, 
# write the logic that asks a player to guess a letter and displays letters in the clue word 
# that were guessed correctly. For now, let the player guess an infinite number of times until they
#  get the entire word. As a bonus, keep track of the letters the player guessed and display a different 
# message if the player tries to guess that letter again. 
# Remember to stop the game when all the letters have been guessed correctly!

def guess_letters(word):
    guessed_letters = []
    clue = ["_"] * len(word)
    attempts = 0
    while "_" in clue:
        guess = input("Guess a letter: ").upper()
        if guess in guessed_letters:
            print("You have already guessed the letter {}".format(guess))
        elif guess in word:
            print("Correct guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    clue[i] = guess
            print("".join(clue))
            guessed_letters.append(guess)
        else:
            print("Incorrect guess!")
            attempts += 1
            print("You have {} incorrect guesses left".format(6 - attempts))
            if attempts == 6:
                print("You have used all your attempts. The word was {}".format(word))
                break
                       
    print("Congratulations! You guessed the word {}".format(word))

if __name__ == "__main__":
    word = "EVAPORATE"
    guess_letters(word)