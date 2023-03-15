import os
import platform

if platform.system() == 'Windows':
    CLEAR = 'cls'
else:
    CLEAR = 'clear'

continueGame = True

board = ['0','1','2','3','4','5','6','7','8']
player1_symbol = ''
player2_symbol = ''

# Printing Board
def print_board():
    output = ""
    for count, board_piece in enumerate(board):
        output += f"  {board_piece}  |" 
        if count % 3 == 2:
            print(output[:-1])
            output = ""
            if count != 8:
                print("- - - - - - - - -")

# Checks for winner
def check_for_winner():
    # Checking Horizontals
    for i in range(0,9,3):
        if board[i] == board[1+i] and board[i] == board[i+2]:
            return True
    # Checking Verticals
    for i in range(0,3):
        if board[i] == board[i+3] and board[i] == board[i + 6]:
            return True
    # Checking Diagonals
    if board[0] == board[4] and board[0] == board[8]:
        return True
    if board[2] == board[4] and board[2] == board[6]:
        return True
    return False

def process_player():
    while True:
        try:
            user_input = int(input("Please select a location between 0 to 8."))
            if user_input < 0 or user_input > 8:
                print("Out of bounds selection. Please try again!")
                continue
            if board[user_input] == 'X' or board[user_input] == 'O':
                print("This spot has already been taking. Please try another spot!")
                continue
            board[user_input] = player1_symbol
            break;
        except ValueError:
            print("Please enter an integer between 0 and 8!")



# Getting user input for symbol
print("Welcome to the Tic-Tac-Toe Game!")
user_input = input("Player 1: Would you like to be 'X' or 'O'?\n").lower()
if user_input == "x":
    player1_symbol = 'X'
    player2_symbol = 'O'
elif user_input == "o":
    player1_symbol = 'O'
    player2_symbol = 'X'
else:
    print("Incorrect input")
    sys.exit()

print_board()
process_player()
os.system(CLEAR)
print_board()


    