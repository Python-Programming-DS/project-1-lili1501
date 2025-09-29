#To display the board status
def display_board(board):
    for i in range(6,0,-1):
        print(f"| {i} | {board[i-1][0]} | {board[i-1][1]} | {board[i-1][2]} | {board[i-1][3]} | {board[i-1][4]} | {board[i-1][5]} | {board[i-1][6]} |")
        print("-"*33)
    print("|R/C| a | b | c | d | e | f | g |")
    print("-"*33)

#To reset the board whenever called 
def reset_board(board):
    for i in range(6):
        for j in range(7):
            board[i][j] = " "
    return board