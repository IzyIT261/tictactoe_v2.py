import random
random.seed()   #Prepare random number generator

board = [""] * (9)

gameOver = False
winner = "None"
for i in range(0, 8 + 1, 1):
    board[i] = " "
i = int(random.random() * 2)
if i == 0:
    currentPlayer = "O"
else:
    currentPlayer = "X"
while gameOver == False:
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])
    if currentPlayer == "O":
        validMove = False
        while validMove == False:
            move = int(input())
            if move >= 1 and move <= 9:
                if board[move - 1] == " ":
                    validMove = True
                else:
                    print("That cell is already occupied. Try again.")
            else:
                print("Invalid cell. Enter a number from 1 to 9")
    else:
        validMove = False
        while validMove == False:
            move = int(random.random() * 9) + 1
            if board[move - 1] == " ":
                validMove = True
    board[move - 1] = currentPlayer
    winner = "None"
    if board[0] != " " and board[0] == board[1] and board[1] == board[2]:
        winner = board[0]
    else:
        if board[3] != " " and board[3] == board[4] and board[4] == board[5]:
            winner = board[3]
        else:
            if board[6] != " " and board[6] == board[7] and board[7] == board[8]:
                winner = board[6]
            else:
                if board[0] != " " and board[0] == board[3] and board[3] == board[6]:
                    winner = board[0]
                else:
                    if board[1] != " " and board[1] == board[4] and board[4] == board[7]:
                        winner = board[1]
                    else:
                        if board[2] != " " and board[2] == board[5] and board[5] == board[8]:
                            winner = board[2]
                        else:
                            if board[0] != " " and board[0] == board[4] and board[4] == board[8]:
                                winner = board[0]
                            else:
                                if board[2] != " " and board[2] == board[4] and board[4] == board[6]:
                                    winner = board[2]
    if winner != "None":
        print(winner + " wins!")
        gameOver = True
    else:
        filledCount = 0
        for i in range(0, 8 + 1, 1):
            if board[i] != " ":
                filledCount = filledCount + 1
        if filledCount == 9:
            print("The game is a draw.")
            gameOver = True
        else:
            if currentPlayer == "O":
                currentPlayer = "X"
            else:
                currentPlayer = "O"
