
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
] 



while True:
    user1_input = input("User 1 Enter the coordinates for row and column (eg ; 1,1 - 3,3): ")
    i = int(user1_input.split(",")[0])-1
    j = int(user1_input.split(",")[1])-1
    if matrix[i][j] == 0:
        matrix[i][j] = "X"
    else:
        print("Already occupied")
        print("\n")

    print(matrix)
    print("\n")
    if matrix[0][0] == "X" and matrix[0][1] == "X" and matrix[0][2] == "X" or matrix[1][0] == "X" and matrix[1][1] == "X" and matrix[1][2] == "X" or matrix[2][0] == "X" and matrix[2][1] == "X" and matrix[2][2] == "X" or matrix[0][0] == "X" and matrix[1][0] == "X" and matrix[2][0] == "X" or matrix[0][1] == "X" and matrix[1][1] == "X" and matrix[2][1] == "X" or matrix[0][2] == "X" and matrix[1][2] == "X" and matrix[2][2] == "X" or matrix[0][0] == "X" and matrix[1][1] == "X" and matrix[2][2] == "X" or matrix[0][2] == "X" and matrix[1][1] == "X" and matrix[2][0] == "X":
        print("***** ---- User 1 wins ----- *****")
        break

    print("\n")
    user2_input = input("User2 Enter the coordinates for row and column (eg ; 1,1 - 3,3): ")
    i = int(user2_input.split(",")[0])-1
    j = int(user2_input.split(",")[1])-1
    if matrix[i][j] == 0:
        matrix[i][j] = "O"
    else:
        print("Already occupied")
        print("\n")
    print(matrix)
    print("\n")
    if matrix[0][0] == "O" and matrix[0][1] == "O" and matrix[0][2] == "O" or matrix[1][0] == "O" and matrix[1][1] == "O" and matrix[1][2] == "O" or matrix[2][0] == "O" and matrix[2][1] == "O" and matrix[2][2] == "O" or matrix[0][0] == "O" and matrix[1][0] == "O" and matrix[2][0] == "O" or matrix[0][1] == "O" and matrix[1][1] == "O" and matrix[2][1] == "O" or matrix[0][2] == "O" and matrix[1][2] == "O" and matrix[2][2] == "O" or matrix[0][0] == "O" and matrix[1][1] == "O" and matrix[2][2] == "O" or matrix[0][2] == "O" and matrix[1][1] == "O" and matrix[2][0] == "O":
        print("***** ---- User 2 wins ----- *****")
        break
    if "0" not in str(matrix):
        print("!!!!! ---- It's a draw ---- !!!!!")
        break

    
