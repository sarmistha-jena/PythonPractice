# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes 
# (8x8 for chess, 19x19 for Go, and many more).

# Ask the user what size game board they want to draw, and draw it for them to the screen 
# using Python’s print statement.

#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- --- 

size_input = input("Enter the size of the game board: ").lower()
size_col = int(size_input.split('x')[0])
size_row = int(size_input.split('x')[1])

for i in range(size_row):
    print(" ---" * size_col)
    print("|   " * (size_col + 1))


print(" ---" * size_col)