#User, will have in your head a number between 0 and 100. The program will guess a number, and you,
#  the user, will say whether it is too high, too low, or your number.
#At the end of this exchange, your program should print out how many guesses it took to get your number.

#As the writer of this program, you will have to choose how your program will strategically guess. 
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you 
# hit the number. But that’s not an optimal guessing strategy. An alternate strategy might be to guess 
# 50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written 
# the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with 
# the solution.)

user_num = int(input("Enter a number between 0 and 100: "))

gussed_num = 50
min_num = 0
max_num = 100
count = 1
while True:
    if gussed_num == user_num:
        print("Your number is {}".format(gussed_num))
        print("I guessed it in {} tries".format(count))
        break
    elif gussed_num < user_num:
        print("Too low")
        print(gussed_num)
        min_num = gussed_num
        gussed_num = int((max_num + min_num) / 2)
    else:
        print("Too high")
        print(gussed_num)
        max_num = gussed_num
        gussed_num = int((max_num + min_num) / 2)
    count += 1