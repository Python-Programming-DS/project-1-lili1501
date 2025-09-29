#To check if it's draw
def checkFull(board):
    for i in range(6):
        for j in range(7):
            if board[i][j]==" ":
                return False
    print("\nDRAW NOBODY WINS!")
    return True

#To check if there is a winner player
def checkWin(board,turn):

    # 6 rows and 7 cols, check each row for 4 continuous 'X' or 'O'
    for i in range(6):
        for j in range(4):
             if board[i][j] == turn and board[i][j+1] == turn and board[i][j+2] == turn and board[i][j+3] == turn:
                print(f"\n{turn} is the winner!")
                return True

    # 6 rows and 7 cols, check each column for 4 continuous 'X' or 'O'
    for i in range(7):
        for j in range(3):
            if board[j][i] == turn and board[j+1][i] == turn and board[j+2][i] == turn and board[j+3][i] == turn:
                print(f"\n{turn} is the winner!")
                return True
                
    #checking the diagnols from forward direction
    for i in range(3):
        for j in range(4):
            if board[i][j]==turn and board[i+1][j+1]==turn and board[i+2][j+2]==turn and board[i+3][j+3]==turn:
                print(f"\n{turn} is the winner!")
                return True
                            
    #checking the diagnols from backward direction
    for i in range(5,2,-1):
        for j in range(4):
            if board[i][j]==turn and board[i-1][j+1]==turn and board[i-2][j+2]==turn and board[i-3][j+3]==turn:
                print(f"\n{turn} is the winner!")
                return True
    return False

#To end the game if there is a winner or board is full
def checkEnd(board,turn):
    if checkWin(board,turn)==True:
        return True
    elif checkFull(board):
        return True
    else:
        return False


