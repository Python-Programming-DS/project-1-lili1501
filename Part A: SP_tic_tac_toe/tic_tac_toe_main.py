# File: tic_tac_toe_main.py
# A 2 player program built to play tic tac toe
# File Used in main.py
#.    1.board_check.py (The following py file check if it's draw/Win )
#.    2.board_status.py (The following py file display/reset the board)
# By: Shesadree Priyadarshani

from board_status import display_board, reset_board
from board_check import checkEnd

#To validate the entry
def validateEntry(row, col, board):

    # Check if row and col entered are in range
    if row < 0 or row > 2 or col < 0 or col >2:
        print(f"Invalid entry: try again.\nRow & column numbers must be either 0, 1, or 2.")

    # Check if the cell is available
    elif board[row][col] != " ":
        print(f"That cell is already taken.\nPlease make another selection.")

    else:
        print("Thankyou for your selection")
        return True
    return False


def main():
    
    #Initializing the board (2D list - 3X3 board)
    board = list()
    for i in range(3):
        board.append([" "] * 3)

    another_game = 'y'
    #Initializing a new game
    while another_game.lower() == 'y':
        
        print("New Game: X goes first\n")
        board = reset_board(board)
        display_board(board)
        End_game = False
        turn = 'X'

        #Starting the game
        while End_game != True: 
            print(f"\n{turn}'s turn")
            print(f"Where do you want your {turn} placed?")

            #To highlight the user input as red
            print("\033[0mPlease enter row number and column number separated by a comma:\033[91m", end="\n")
            row, col = map(int, input().split(","))

            #To bring back the terminal back to default color text
            print("\033[0m", end="")
            print(f"You have entered row #{row}\n\t  and column #{col}")

            if validateEntry(row, col, board) == True:
                board[row][col] = turn

                if checkEnd(board, turn)==True:
                    End_game = True 

                display_board(board)   
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'

        print("\n\033[0mAnother game? Enter Y or y for yes:\033[91m", end="\n")
        another_game = input()
        print("\033[0m", end="")

    print("Thank you for playing!")
    
if __name__ == "__main__":
    main()   