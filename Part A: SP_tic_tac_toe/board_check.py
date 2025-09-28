#to check if board is full
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


def checkFull(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                return False
    print("\nDRAW NOBODY WINS!")
    return True


def checkEnd(board, turn):
    if checkWin(board,turn)== True :
        return True
    elif checkFull(board)==True:
        return True
    else:
        return False

