import random
import os
import platform

class Game:

    def __init__(self):
        self.continueGame = True
        self.board = ['0','1','2','3','4','5','6','7','8']
        self.player1_symbol = ''
        self.player2_symbol = ''
        self.player1_turn = False
        self.player2_turn = False
        self.player1_status = False
        self.player2_status = False

        # Getting user's input
        print("Welcome to the Tic-Tac-Toe Game!")
        user_input = input("Player 1: Would you like to be 'X' or 'O'?\n").lower()
        while True:
            if user_input == "x":
                self.player1_symbol = 'X'
                self.player2_symbol = 'O'
                break
            elif user_input == "o":
                self.player1_symbol = 'O'
                self.player2_symbol = 'X'
                break
            else:
                print("Incorrect input. Please try again!")

    # Processing player's turn
    def process_player_turn(self):
        if self.player1_turn:
            print("Player 1's turn!")
            player_symbol = self.player1_symbol
            self.player1_turn = False
            self.player2_turn = True
        elif self.player2_turn:
            print("Player 2's turn!")
            player_symbol = self.player2_symbol
            self.player1_turn = True
            self.player2_turn = False
        while True:
            try:
                user_input = int(input("Please select a location between 0 to 8."))
                if user_input < 0 or user_input > 8:
                    print("Out of bounds selection. Please try again!")
                    continue
                if self.board[user_input] == 'X' or self.board[user_input] == 'O':
                    print("This spot has already been taking. Please try another spot!")
                    continue
                self.board[user_input] = player_symbol
                break;
            except ValueError:
                print("Please enter an integer between 0 and 8!")

    # Randomize who will start the game first
    def randomize_initial_turn(self):
        random_number = random.randint(0,1)
        if random_number == 0:
            self.player1_turn = True
            print("Player 1 will be starting first!")
        else:
            self.player2_turn = True
            print("Player 2 will be starting first!")
    
    # Printing Board
    def print_board(self):
        output = ""
        for count, board_piece in enumerate(self.board):
            output += f"  {board_piece}  |" 
            if count % 3 == 2:
                print(output[:-1])
                output = ""
                if count != 8:
                    print("- - - - - - - - -")

    # Checks for winner
    def check_for_winner(self):
        # Checking Horizontals
        for i in range(0,9,3):
            if self.board[i] == self.board[1+i] and self.board[i] == self.board[i+2]:
                self.print_winner(self.board[i])
                return True
        # Checking Verticals
        for i in range(0,3):
            if self.board[i] == self.board[i+3] and self.board[i] == self.board[i + 6]:
                self.print_winner(self.board[i])
                return True
        # Checking Diagonals
        if self.board[0] == self.board[4] and self.board[0] == self.board[8]:
            self.print_winner(self.board[0])
            return True
        if self.board[2] == self.board[4] and self.board[2] == self.board[6]:
            self.print_winner(self.board[2])
            return True
        return False

    # Checks for draw
    def check_for_draw(self):
        for board_piece in self.board:
            if board_piece != "X" and board_piece != "O":
                return False
        self.print_draw()
        return True

    # Clears player screen
    def clear_screen(self):
        if platform.system() == 'Windows':
            CLEAR = 'cls'
        else:
            CLEAR = 'clear'
        os.system(CLEAR)

    # Prints who the winner was
    def print_winner(self, winning_board_piece: str):
        self.print_board()
        print("GAME OVER!")
        if winning_board_piece == self.player1_symbol:
            self.player1_status = True
            print("The winner is Player 1!")
        elif winning_board_piece == self.player2_symbol:
            self.player1_status = True
            print("The winner is Player 2!")

    def print_draw(self):
        self.print_board()
        print("GAME OVER!")
        print("There was no winner. Game ended in a stalemate/draw!")
