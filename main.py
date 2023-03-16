from game import Game

game = Game()
game.randomize_initial_turn()

while not game.check_for_winner() and not game.check_for_draw():
    game.print_board()
    game.process_player_turn()
    game.clear_screen()