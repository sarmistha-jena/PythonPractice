# If a game of Tic Tac Toe is represented as a list of lists, like so:

# game = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space, 
# and a 2 means that player 2 put their token in that space.

# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, 
# tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row
#  - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won
#  - assume that in every board there will only be one winner.

matrix = [
    [2, 2, 1],
    [2, 1, 1],
    [2, 1, 1]
]   
winner = 0
for i in range(3):
    if matrix[i][0] == matrix[i][1] == matrix[i][2] != 0:
        winner = matrix[i][0]
        break
    if matrix[0][i] == matrix[1][i] == matrix[2][i] != 0:
        winner = matrix[0][i]
        break
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != 0:
        winner = matrix[0][0]
        break
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != 0:
        winner = matrix[0][2]
        break
if winner != 0:
    print(f"Player {winner} wins!")



