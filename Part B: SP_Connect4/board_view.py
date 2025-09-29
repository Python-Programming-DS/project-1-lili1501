board = list()
for i in range(6):
     board.append([" "] * 7)

def display_board(board):
    for i in range(6,0,-1):
        print(f"| {i} | {board[i-1][0]} | {board[i-1][1]} | {board[i-1][2]} | {board[i-1][3]} | {board[i-1][4]} | {board[i-1][5]} | {board[i-1][6]} |")
        print("-"*33)
    print("|R/C| a | b | c | d | e | f | g |")
    print("-"*33)
    
def reset_board(board):
    for i in range(6):
        for j in range(7):
            board[i][j] = " "
    return board


def col_row_num(pos):
    row = int(pos[1])-1
    col = ord(pos[0].lower()) - ord('a')

    return row,col

def col_letter_row(row,col):
    col_alpha = chr(col + ord('a'))
    row_str = str(row+1)
    pos = col_alpha + row_str
    return pos

def init_avail_pos():
    col = ['a','b','c','d','e','f','g']
    available = []
    for i in range(len(col)):
        available.append(f"{col[i]}{1}")

    return available
available = init_avail_pos()

def available_position(board,available):
    upd_available = []
    for i in range(len(available)):
        cell = available[i]
        row, col = col_row_num(cell)
        while row < len(board) and board[row][col] != " ":
            row += 1
        if row < len(board): 
            upd_available.append(col_letter_row(row, col))
    return upd_available


# row, col = col_letter_row_num('f4')
# board[row][col] = "X"

# display_board(board)
# print(f"after resetting:")
# board = reset_board(board)
# display_board(board)
# pos = available_position(board)
# print(pos)