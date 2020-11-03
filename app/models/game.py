from app.models.player import *

class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def player_move(self, result):
        if result == "rock":
            return 0
        elif result == "paper":
            return 1
        elif result == "scissors":
            return 2
            
    def print_winner(self, winning_player):
        return f"{winning_player.name} wins by playing {winning_player.choice}!"

    def tie(self):
        return "Tie Game!"
        
    def play_new_game(self, player1, player2):
        
        # game_map = {0:"rock", 1:"paper", 2:"scissors"}
        rps_table = [[None, 1, 0], [1, None, 2],[0, 2, None]]
        winner = rps_table[self.player_move(player1.choice)][self.player_move(player2.choice)]

        if winner == self.player_move(player1.choice):
            return self.print_winner(player1)
        elif winner == self.player_move(player2.choice):
            return self.print_winner(player2)
        else:
            return self.tie()

    def select_icon(self, player):
        player.choice
        return "header > h1 {color: hotpink;}"

    
