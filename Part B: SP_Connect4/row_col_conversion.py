#Converting the alpha-numeric user input (Eg, a1,c1...) to row col integer value (Eg, (0,0),(0,3))
def col_row_num(pos):
    row = int(pos[1])-1
    col = ord(pos[0].lower()) - ord('a')

    return row,col

#Converting the row col integer value to alpha-numeric (Eg, a1,b2,d4....)
def col_letter_row(row,col):
    col_alpha = chr(col + ord('a'))
    row_str = str(row+1)
    pos = col_alpha + row_str
    return pos
