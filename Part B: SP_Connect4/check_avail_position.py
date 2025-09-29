#importing required function from row_col_conversion.py file
from row_col_conversion import col_letter_row,col_row_num 

#Initializing the available position(botton rows)
def init_avail_pos():
    col = ['a','b','c','d','e','f','g']
    available = []
    for i in range(len(col)):
        available.append(f"{col[i]}{1}")

    return available
available = init_avail_pos()

#Updating the available position list based on user selection in the main.py file
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
