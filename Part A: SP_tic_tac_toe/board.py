def display_board(board):
    print("-"*23)
    for i in range(4):
        if i == 0:
            print(f"|R\\C|  {i}  |  {i+1}  |  {i+2}  |")
        print("-"*23)
        if i <3:
            print(f"| {i} |  {board[i][0]}  |  {board[i][1]}  |  {board[i][2]}  |")


def reset_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
    return board

