# File: connect4_main.py
# A 2 player program built to play connect four
# The first player to get 4's in row, col, diagnol wins
# File Used in main.py
#.    1.board_check.py (The following py file check if it's draw/Win )
#.    2.board_view.py (The following py file display/reset the board)
#.    3.check_avail_position.py (The py file check the position available for player to choose )
#.    4.row_col_conversion.py (The py file converts the alpa numeric position to integer value)
# By: Shesadree Priyadarshani 

from board_view import *
from row_col_conversion import *
from check_avail_position import *
from board_check import checkEnd

#To validate the entry
def validateEntry(row, col, pos,board,available):

    # Check if the user has selected from the available list
    # Check if row and col entered are in range
    if (pos not in available) or (row < 0 or row > 6 or col < 0 or col >7):
        print(f"Invalid entry: try again.\nPlease input from the available position displayed")

    # Check if the cell is available
    elif board[row][col] != " ":
        print(f"That cell is already taken.\nPlease make another selection from the available position displayed.")
    
    else:
        print("Thankyou for your selection")
        return True
    return False

def main():
    board = list()
    for i in range(6):
        board.append([" "] * 7)
    
    another_game = 'y'
    #Intialize a new game
    while another_game.lower() == 'y':
       
        print("New Game: X goes first\n")
        board = reset_board(board)
        display_board(board)
        End_game = False
        turn = 'X'

        #To get the initial bottom places in the board
        available = init_avail_pos()

        #Start Game
        while End_game != True: 
            print(f"\n{turn}'s turn")
            print(f"Where do you want your {turn} placed?")

            #To update the position availability based on user choice
            available = available_position(board,available)
            print(f"Available Positions are : {available}\n")

            pos = input("Please enter column-letter and row-number (e.g., a1): ")
            row, col = col_row_num(pos)

            if validateEntry(row, col,pos, board,available) == True:
                board[row][col] = turn
                
                if checkEnd(board, turn)==True:
                    End_game = True 
                
                display_board(board)   
                
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
        
        another_game = input("\nAnother game (y/n)? ")

    print("Thank you for playing!")
    
if __name__ == "__main__":
    main()   