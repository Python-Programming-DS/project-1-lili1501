from board import display_board, reset_board
from board_check import checkEnd

#to validate the entry
def validateEntry(row, col, board):
    # Check if row and col entered are in range
    if row < 0 or row > 2 or col < 0 or col >2:
        print(f"Invalid entry: try again.\nRow & column numbers must be either 0, 1, or 2")
    # Check if the cell is available
    elif board[row][col] != " ":
        print(f"That cell is already taken.\nPlease make another selection.")
    else:
        print("Thankyou for your selection")
        # display_board(board)
        return True
    return False


def main():
    
    #Initializing the board (2D list)
    board = list()
    for i in range(3):
        board.append([" "] * 3)

    another_game = 'y'
    while another_game.lower() == 'y':
        print("New Game: X goes first\n")
        board = reset_board(board)
        display_board(board)
        End_game = False
        turn = 'X'
        while End_game != True: 
            print(f"\n{turn}'s turn")
            print(f"Where do you want your {turn} placed?")
            print("\033[0mPlease enter row number and column number separated by a comma:\033[91m", end="\n")
            row, col = map(int, input().split(","))
            print("\033[0m", end="")
            print(f"You have entered row #{row}\n\t  and column #{col}")
            if validateEntry(row, col, board) == True:
                board[row][col] = turn
                if checkEnd(board, turn)==True:
                    # display_board(board)
                    End_game = True 
                display_board(board)   
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
        print("\n\033[0mAnother game? Enter either Y or y for yes:\033[91m", end="\n")
        another_game = input()
        print("\033[0m", end="")
    print("Thank you for playing!")
    
if __name__ == "__main__":
    main()   