from game import Game
import time

game = Game()
game.randomize_initial_turn()

while not game.check_for_winner() and not game.check_for_draw():
    game.print_board()
    game.process_player_turn()
    if game.bot_active and game.player1_turn:
        time.sleep(1)
    game.clear_screen()