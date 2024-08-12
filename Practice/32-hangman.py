def pick_word():
    import random
    with open("sowpods.txt", "r") as f:
        words = f.readlines()
        return random.choice(words).strip()

def guess_letters(word):
    guessed_letters = []
    clue = ["_"] * len(word)
    attempts = 6
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
            attempts -= 1
            draw_hangman(attempts)
            if attempts == 0:
                print("You have used all your attempts. The word was {}".format(word))
                break
        #print("Congratulations! You guessed the word {}".format(word))               
#draw a hangman animation.  In the game of Hangman, 
# the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.
def draw_hangman(attempts):
    print("  ____")
    print(" |    |")
    if attempts == 0:
        print(" |")
        print(" |")
        print(" |")
    elif attempts == 1:
        print(" |    O")
        print(" |")
        print(" |")
    elif attempts == 2:
        print(" |    O")
        print(" |    |")
        print(" |")
    elif attempts == 3:
        print(" |    O")
        print(" |   /|")
        print(" |")
    elif attempts == 4:
        print(" |    O")
        print(" |   /|\\")
        print(" |")
    elif attempts == 5:
        print(" |    O")
        print(" |   /|\\")
        print(" |   /")
    print(" |")
    print("_|_")
    
    
    

def hangman():
    print("Welcome to Hangman!")
    
    while True:
        choice = input("Do you want to play? (y/n) ").lower()
        if choice == "y":
            word = pick_word()
            guess_letters(word)
        else:
            print("Maybe next time")
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    hangman()