import random
import os
import platform

class Game:

    def __init__(self):
        self.continueGame = True
        self.board = ['1','2','3','4','5','6','7','8','9']
        self.bot_active = False
        self.player1_symbol = ''
        self.player2_symbol = ''
        self.bot_symbol = ' '
        self.player1_turn = False
        self.player2_turn = False
        self.bot_turn = False
        self.player1_status = False
        self.player2_status = False
        self.bot_status = False

        # Gets the user's input to start the game
        print("Welcome to the Tic-Tac-Toe Game!")
        while True:
            user_input = input("Would you like to play against a friend (taking turns) or against a bot? Y - Friend | N - Bot\n").lower()
            if user_input == 'y':
                self.bot_active = False
                self.process_players_symbol()
                break
            elif user_input == 'n':
                self.bot_active = True
                self.process_players_symbol()
                break
            else:
                print("Invalid input. Please try again!")

    # Gets the user's input for which symbol they would like to be
    def process_players_symbol(self):
        user_input = input("Player 1: Would you like to be 'X' or 'O'?\n").lower()
        while True:
            if user_input == "x":
                self.player1_symbol = 'X'
                if self.bot_active:
                    self.bot_symbol = 'O'
                else:
                    self.player2_symbol = 'O'
                break
            elif user_input == "o":
                self.player1_symbol = 'O'
                if self.bot_active:
                    self.bot_symbol = 'X'
                else:
                    self.player2_symbol = 'X'
                break
            else:
                print("Invalid input. Please try again!")

    # Randomize who will start the game first
    def randomize_initial_turn(self):
        random_number = random.randint(0,1)
        if random_number == 0:
            self.player1_turn = True
            print("Player 1 will be starting first!")
        else:
            if self.bot_active:
                self.bot_turn = True
                print("The Bot will be starting soon!")
            else:
                self.player2_turn = True
                print("Player 2 will be starting first!")

    # Processing player's turn
    def process_player_turn(self):
        if self.player1_turn:
            print("Player 1's turn!")
            self.get_player_turn()
            player_symbol = self.player1_symbol
            self.player1_turn = False
            if self.bot_active:
                self.bot_turn = True
            else:
                self.player2_turn = True
        else:
            if self.player2_turn:
                print("Player 2's turn!")
                self.get_player_turn()
                player_symbol = self.player2_symbol
                self.player1_turn = True
                self.player2_turn = False
            elif self.bot_turn:
                print("Bot's turn!")
                self.player1_turn = True
                self.bot_turn = False
                self.process_bot_turn()

    # Gets the players' input for their selection on the board
    def get_player_turn(self):
        if self.player1_turn:
            player_symbol = self.player1_symbol
        elif self.player2_turn:
            player_symbol = self.player2_symbol
        while True:
            try:
                user_input = int(input("Please select a location between 1 to 9.\n"))
                if user_input < 1 or user_input > 9:
                    print("Out of bounds selection. Please try again!")
                    continue
                if self.board[user_input - 1] == 'X' or self.board[user_input - 1] == 'O':
                    print("This spot has already been taking. Please try another spot!")
                    continue
                self.board[user_input - 1] = player_symbol
                break;
            except ValueError:
                print("Please enter an integer between 0 and 8!")

    # Processess the bot's turn
    def process_bot_turn(self):
        if self.check_bot_winning_move():
            return
        potential_blocking_position = self.check_player_winning_move()
        if potential_blocking_position != -1:
            self.make_bot_turn(potential_blocking_position)
            return
        if self.check_corners():
            return
        if self.check_center():
            return
        if self.check_sides():
            return
        
    # Places the bot's decision
    def make_bot_turn(self, position: int):
        self.board[position] = self.bot_symbol

    def check_bot_winning_move(self):
         # Checking Horizontals
        for i in range(0,9,3):
            if self.board[i] == self.board[1+i] and self.board[i] == self.bot_symbol and self.check_space(i+2):
                self.make_bot_turn(i+2)
                return True
            elif self.board[i] == self.board[i+2] and self.board[i] == self.bot_symbol and self.check_space(i+1):
                self.make_bot_turn(i+1)
                return True
        # Checking Verticals
        for i in range(0,3):
            if self.board[i] == self.board[i+3] and self.board[i] == self.bot_symbol and self.check_space(i+6):
                self.make_bot_turn(i+6)
                return True
            elif self.board[i] == self.board[i+6] and self.board[i] == self.bot_symbol and self.check_space(i+3):
                self.make_bot_turn(i+3)
                return True
        # Checking Diagonals
        if self.board[0] == self.board[4] and self.board[0] == self.bot_symbol and self.check_space(8):
            self.make_bot_turn(8)
            return True
        if self.board[0] == self.board[8] and self.board[0] == self.bot_symbol and self.check_space(4):
            self.make_bot_turn(4)
            return True
        if self.board[2] == self.board[4] and self.board[2] == self.bot_symbol and self.check_space(6):
            self.make_bot_turn(6)
            return True
        if self.board[2] == self.board[6] and self.board[0] == self.bot_symbol and self.check_space(4):
            self.make_bot_turn(4)
            return True
        return False

    # Checks to see if the player has a winning move
    def check_player_winning_move(self):
        # Checking Horizontals
        for i in range(0,9,3):
            if self.board[i] == self.board[1+i] and self.board[i] == self.player1_symbol and self.check_space(i+2):
                return i+2
            elif self.board[i] == self.board[i+2] and self.board[i] == self.player1_symbol and self.check_space(i+1):
                return i+1
        # Checking Verticals
        for i in range(0,3):
            if self.board[i] == self.board[i+3] and self.board[i] == self.player1_symbol and self.check_space(i+6):
                return i+6
            elif self.board[i] == self.board[i+6] and self.board[i] == self.player1_symbol and self.check_space(i+3):
                return i+3
        # Checking Diagonals
        if self.board[0] == self.board[4] and self.board[0] == self.player1_symbol and self.check_space(8):
            return 8
        if self.board[0] == self.board[8] and self.board[0] == self.player1_symbol and self.check_space(4):
            return 4
        if self.board[2] == self.board[4] and self.board[2] == self.player1_symbol and self.check_space(6):
            return 6
        if self.board[2] == self.board[6] and self.board[0] == self.player1_symbol and self.check_space(4):
            return 4
        return -1

    # Checks corners for bot
    def check_corners(self):
        corners_free = []
        for i in range(0,9):
            if i % 2 == 0 and i != 4 and self.check_space(i):
                corners_free.append(i)
        if not corners_free:
            return False
        else:
            self.make_bot_turn(random.choice(corners_free))
            return True
        
    # Checks center for bot
    def check_center(self):
        if self.check_space(4):
            self.make_bot_turn(4)
            return True
        return False

    # Checks sides for bot
    def check_sides(self):
        sides_free = []
        for i in range(0,9):
            if i % 2 == 1 and self.check_space(i):
                sides_free.append(i)
        if not sides_free:
            return False
        else:
            self.make_bot_turn(random.choice(corners_free))
            return True

    # Checks space for bot
    def check_space(self, position: int):
        if self.board[position] != self.player1_symbol and self.board[position] != self.bot_symbol:
            return True
        return False

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

    # Checks for draw
    def check_for_draw(self):
        for board_piece in self.board:
            if board_piece != "X" and board_piece != "O":
                return False
        self.print_draw()
        return True

    # Prints who the winner was
    def print_winner(self, winning_board_piece: str):
        self.print_board()
        print("GAME OVER!")
        if winning_board_piece == self.player1_symbol:
            self.player1_status = True
            print("The winner is Player 1!")
        elif winning_board_piece == self.player2_symbol:
            self.player2_status = True
            print("The winner is Player 2!")
        elif winning_board_piece == self.bot_symbol:
            self.bot_status = True
            print("The winner is the Bot!")

    # Print if there was a stalemate/draw
    def print_draw(self):
        self.print_board()
        print("GAME OVER!")
        print("There was no winner. Game ended in a stalemate/draw!")

    # Clears player screen
    def clear_screen(self):
        if platform.system() == 'Windows':
            CLEAR = 'cls'
        else:
            CLEAR = 'clear'
        os.system(CLEAR)
