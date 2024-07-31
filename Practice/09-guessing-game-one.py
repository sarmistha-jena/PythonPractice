#Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random


num = random.randint(1,9)
def guess(num):
    userinput = int(input("Guess a number between 1 and 9: "))
    if userinput < num:
        print(">>>>>>Too low<<<<<<<")
        return("Too low")
    elif userinput > num:
        print("<<<<<<Too high>>>>>>")
        return("Too high")
    else:
        print("*****Exactly right*****")
        return("Exactly right")
        
while True:
    #guess(num)
    #print(guess(num))
    if guess(num)=="Exactly right":
        break

print("The random number is {}".format(num))
