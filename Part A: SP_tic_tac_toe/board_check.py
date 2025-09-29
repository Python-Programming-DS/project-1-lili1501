#To check if there is winner player
def checkWin(board, turn):
    for i in range(3):
        if i == 0:
            if board[i][i] == turn and board[i+1][i+1] == turn and board[i+2][i+2] == turn:
                print(f"{turn} IS THE WINNER!")
                return True
            if board[i][i+2] == turn and board[i+1][i+1] == turn and board[i+2][i] == turn:
                print(f"{turn} IS THE WINNER!")
                return True
        if board[i][0] == turn and board[i][1] == turn and board[i][2] == turn:
            print(f"{turn} IS THE WINNER!")
            return True
        if board[0][i] == turn and board[1][i] == turn and board[2][i] == turn:
            print(f"{turn} IS THE WINNER!")
            return True
    return False


#To check if the board is full/it's draw
def checkFull(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                return False
    print("\nDRAW NOBODY WINS!")
    return True


#To end the game if a player wins or if the board is full
def checkEnd(board, turn):
    if checkWin(board,turn)== True :
        return True
    elif checkFull(board)==True:
        return True
    else:
        return False

